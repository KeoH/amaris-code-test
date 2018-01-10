
from django.utils.translation import gettext_lazy as _

ROLE_CHOICES = [
    ('1', _('ET::BOSS')),
    ('2', _('ET::TECNIC')),
    ('3', _('ET::STUDENT'))
]

DEPARTAMENT_CHOICES = [
    ('AD', _('DT::ADMINISTRATION')),
    ('PR', _('DT::PROGRAMMING')),
    ('CO', _('DT::COMMERCE'))
]