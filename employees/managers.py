from django.contrib.auth import models


class EmployeeManager(models.UserManager):
    
    def get_queryset(self):
        return super().get_queryset().filter(is_hired=True)

    def get_best_subordinate(self, queryset):
        return queryset.first()

    def average_age(self, queryset):
        total = 0
        for empleyee in queryset:
            total += empleyee.age
        return total/queryset.count()