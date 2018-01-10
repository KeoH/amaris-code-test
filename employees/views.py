from django.shortcuts import render
from django.views.generic import View, TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Employee
from .forms import EmployeeForm

class EmployeeListView(LoginRequiredMixin, View):

    def get(self, request):

        context = {
            'bosses' : Employee.employees.filter(role='1'),
            'tecnics' : Employee.employees.filter(role='2'),
            'students' : Employee.employees.filter(role='3'),
            'bosses_age' : Employee.employees.average_age(Employee.employees.filter(role='1')),
            'tecnics_age' : Employee.employees.average_age(Employee.employees.filter(role='2')),
            'students_age' : Employee.employees.average_age(Employee.employees.filter(role='3')),
            'page' : 'employee'
        }

        return render(request, 'employees/list.html', context)

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'employees/profile.html'


class EmployeeAddView(LoginRequiredMixin, FormView):
    template_name = 'employees/add.html'
    form_class = EmployeeForm
    success_url = '/employees/'

    def get_context_data(self, **kwargs):
        context = super(EmployeeAddView, self).get_context_data(**kwargs)
        context['page'] = 'employee'
        return context

    def form_valid(self, form):
        form.save()
        return super(EmployeeAddView, self).form_valid(form)