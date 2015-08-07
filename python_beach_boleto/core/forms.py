from django import forms
from python_beach_boleto.core.models import Enrollment


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['name', 'email', 'state', 'city', 'institution', 'degree']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Nome',
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Email',
                'type': 'email'
            }),
            'city': forms.TextInput(attrs={
                'placeholder': 'Cidade',
            }),
            'institution': forms.TextInput(attrs={
                'placeholder': 'Instituição',
            }),
            'degree': forms.TextInput(attrs={
                'placeholder': 'Formação',
            }),
        }


class RecoveryPayment(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Email', 'type': 'email'}
        )
    )
