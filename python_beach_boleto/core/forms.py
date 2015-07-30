from django import forms
from python_beach_boleto.core.models import Enrollment


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['name', 'email', 'state', 'city', 'institution', 'degree']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Nome',
                'class': 'pure-input-1-2'
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Email',
                'class': 'pure-input-1-2',
                'type': 'email'
            }),
            'state': forms.Select(attrs={
                'class': 'pure-input-1-2'
            }),
            'city': forms.TextInput(attrs={
                'placeholder': 'Cidade',
                'class': 'pure-input-1-2',
            }),
            'institution': forms.TextInput(attrs={
                'placeholder': 'Instituição',
                'class': 'pure-input-1-2'
            }),
            'degree': forms.TextInput(attrs={
                'placeholder': 'Formação',
                'class': 'pure-input-1-2'
            }),
        }
