from datetime import timedelta, date
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.postgres.fields import JSONField

from .choices import DEPARTAMENT_CHOICES, ROLE_CHOICES
from .managers import EmployeeManager


class Employee(AbstractUser):
    
    departament = models.CharField(
        _('FI::DEPARTAMENT'), max_length=2, choices=DEPARTAMENT_CHOICES, 
        default='AD')
    role = models.CharField(
        _('FI::ROLE'), max_length=2, choices=ROLE_CHOICES, 
        default='2')
    boss = models.ForeignKey(
        'self', related_name='subordinates', blank=True, 
        null=True, on_delete=None, verbose_name=_('FI::BOSS'))
    hired_date = models.DateField(verbose_name=_('FI::HIRED_DATE'), auto_now_add=True)
    is_hired = models.BooleanField(default=True, verbose_name=_('FI::IS_HIRED'))
    is_traveling = models.BooleanField(default=False, verbose_name=_('FI::IS_TRAVELING'))
    traveling_data = JSONField(default={}, verbose_name=_('FI::TRAVELING_DATA'), blank=True)
    birthdate = models.DateField(verbose_name=_('FI:BIRTHDATE'), blank=True, null=True)

    objects = UserManager()
    employees = EmployeeManager()
    
    def promote(self):
        if not self.is_promoted():
            data = self.traveling_data
            data['promote'] = data.get('promote', {'old_role':self.role, 'promotions':[]})
            data.get('promote').get('promotions').append(
                {'new_role': self.boss.role, 'date': timezone.now().strftime('%d/%m/%Y')}
            )
            self.traveling_data = data
            self.role = self.boss.role
            print("{} ha sido promocionado temporalmente a {}.".format(self.username, self.role))
            self.save()

    def permanent_promote(self):
        if not self.is_promoted():
            self.role = str(int(self.role) - 1) if int(self.role) > 1 else '1'
            if self.boss and self.boss.boss:
                self.boss = self.boss.boss
                print("{} ha sido promocionado definitivamente a {}.".format(self.username, self.role))
            else:
                self.boss = None
            if self.subordinates.all():
                self.promote_subordinates()
            self.traveling_data['promote'] = {}
            self.save()
        
    def promote_subordinates(self):
        self.is_traveling = False
        self.permanent_promote()
        for sub in self.subordinates.all():
            sub.promote_subordinates()

    @property
    def is_boss(self):
        return self.role == '1'

    @property
    def age(self):
        if self.birthdate:
            a = date.today() - self.birthdate
            return int(a.days/365)
        return 0

    def left_company(self):
        self.is_traveling = False
        self.is_hired = False
        if self.subordinates.all():
            selected = Employee.employees.get_best_subordinate(self.subordinates)
            print("{}, {} ha dejado la compañía. {} le sustituirá.".format(self.username, self.role, selected.username))
            selected.permanent_promote()
        for subordinate in self.subordinates.exclude(username=selected.username):
            subordinate.boss = selected
            subordinate.save()
        self.boss = None
        self.save()

    def has_promoted(self):
        if self.traveling_data.get('promote'):
            return True
        return False

    def is_promoted(self):
        if self.has_promoted():
            return self.role != self.traveling_data.get('promote').get('old_role')
        return False

    def unpromote(self):
        if self.has_promoted():
            self.role = self.traveling_data.get('promote').get('old_role')
            data = self.traveling_data
            data.get('promote').get('promotions')[-1]['end_date'] = timezone.now().strftime('%d/%m/%Y')
            self.traveling_data = data
            self.save()

    def times_promoted(self):
        if not self.has_promoted():
            return 0
        return len(self.traveling_data.get('promote').get('promotions', []))

    def go_travel(self):
        self.is_traveling = True
        if self.subordinates.all():
            selected = self.subordinates.order_by('-hired_date').first()
            selected.promote()
            if not self.traveling_data.get('substitute'):
                self.traveling_data['substitute'] = selected.username
        self.save()

    def end_travel(self):
        self.is_traveling = False
        if self.subordinates.filter(username=self.traveling_data['substitute']):
            self.subordinates.get(username=self.traveling_data['substitute']).unpromote()
        self.save()

    def save(self, *args, **kwargs):
        if self.is_hired:
            self.hired_date = timezone.now()
        return super(Employee, self).save(*args, **kwargs)
