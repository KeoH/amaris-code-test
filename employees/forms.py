from django import forms
from django.contrib.auth.hashers import make_password
from .models import Employee
from .choices import DEPARTAMENT_CHOICES, ROLE_CHOICES

class EmployeeForm(forms.ModelForm):
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    repeat_password = forms.CharField(required=True, widget=forms.PasswordInput)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    birthdate = forms.DateField(required=True, widget=forms.DateInput)

    class Meta:
        model = Employee
        fields = ['username', 'password', 'repeat_password', 'first_name', 'last_name', 'birthdate','role', 'departament', 'boss']

    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get('password')
        pass2 = cleaned_data.get('repeat_password')
        if pass1 and pass2:
            if pass1 != pass2:
                raise forms.ValidationError('Passwords are not equals!')
        cleaned_data['password'] = make_password(cleaned_data['password'])
        return cleaned_data
