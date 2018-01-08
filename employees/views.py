from django.shortcuts import render
from django.views.generic import View

from django.db.models import Avg
from .models import Employee

class EmployeeListView(View):

    def get(self, request):

        context = {
            'bosses' : Employee.employees.filter(role='1'),
            'tecnics' : Employee.employees.filter(role='2'),
            'students' : Employee.employees.filter(role='3'),
            'bosses_age' : Employee.employees.average_age(Employee.employees.filter(role='1')),
            'tecnics_age' : Employee.employees.average_age(Employee.employees.filter(role='2')),
            'students_age' : Employee.employees.average_age(Employee.employees.filter(role='3')),
        }

        return render(request, 'employees/list.html', context)