from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Employee

class EmployeeListView(LoginRequiredMixin, View):

    def get(self, request):

        context = {
            'bosses' : Employee.employees.filter(role='1'),
            'tecnics' : Employee.employees.filter(role='2'),
            'students' : Employee.employees.filter(role='3'),
            'bosses_age' : Employee.employees.average_age(Employee.employees.filter(role='1')),
            'tecnics_age' : Employee.employees.average_age(Employee.employees.filter(role='2')),
            'students_age' : Employee.employees.average_age(Employee.employees.filter(role='3')),
            'page' : 'employee_list'
        }

        return render(request, 'employees/list.html', context)

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'employees/profile.html'