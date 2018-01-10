from django.shortcuts import get_object_or_404
from django.views.generic import View, TemplateView, FormView
from django.views.generic.base import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Employee
from .forms import EmployeeForm

class EmployeeRoleListView(LoginRequiredMixin, TemplateView):

    template_name = 'employees/roles.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeRoleListView, self).get_context_data(**kwargs)
        context.update({
            'bosses' : Employee.employees.filter(role='1'),
            'tecnics' : Employee.employees.filter(role='2'),
            'students' : Employee.employees.filter(role='3'),
            'bosses_age' : Employee.employees.average_age(Employee.employees.filter(role='1')),
            'tecnics_age' : Employee.employees.average_age(Employee.employees.filter(role='2')),
            'students_age' : Employee.employees.average_age(Employee.employees.filter(role='3')),
            'page' : 'employee'
        })
        return context

class EmployeeDepartamentListView(LoginRequiredMixin, TemplateView):

    template_name = 'employees/departaments.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeDepartamentListView, self).get_context_data(**kwargs)
        context.update({
            'administration' : Employee.employees.filter(departament='AD'),
            'programming' : Employee.employees.filter(departament='PR'),
            'comercial' : Employee.employees.filter(departament='CO'),
            'administration_age' : Employee.employees.average_age(Employee.employees.filter(departament='AD')),
            'programming_age' : Employee.employees.average_age(Employee.employees.filter(departament='PR')),
            'comercial_age' : Employee.employees.average_age(Employee.employees.filter(departament='CO')),
            'page' : 'departament'
        })
        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'employees/profile.html'

class GoTravelView(LoginRequiredMixin, RedirectView):
    pattern_name = 'employee_list'

    def get_redirect_url(self, *args, **kwargs):
        employee = get_object_or_404(Employee, pk=kwargs['pk']).go_travel()
        kwargs.pop('pk')
        return super().get_redirect_url(*args, **kwargs)

class EndTravelView(LoginRequiredMixin, RedirectView):
    pattern_name = 'employee_list'

    def get_redirect_url(self, *args, **kwargs):
        employee = get_object_or_404(Employee, pk=kwargs['pk']).end_travel()
        kwargs.pop('pk')       
        return super().get_redirect_url(*args, **kwargs)

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