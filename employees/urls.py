from django.urls import path

from .views import EmployeeRoleListView, EmployeeAddView, EmployeeDepartamentListView, GoTravelView, EndTravelView

urlpatterns = [
    path('', EmployeeRoleListView.as_view(), name="employee_list"),
    path('department', EmployeeDepartamentListView.as_view(), name="department_list"),
    path('add/', EmployeeAddView.as_view(), name="employee_add"),
    path('<int:pk>/go_travel/', GoTravelView.as_view(), name="go_travel"),
    path('<int:pk>/end_travel/', EndTravelView.as_view(), name="end_travel")
    
]