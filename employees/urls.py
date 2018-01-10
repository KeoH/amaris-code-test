from django.urls import path

from .views import EmployeeListView, EmployeeAddView

urlpatterns = [
    path('', EmployeeListView.as_view(), name="employee_list"),
    path('add/', EmployeeAddView.as_view(), name="employee_add")
]