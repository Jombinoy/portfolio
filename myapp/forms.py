# forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']



# forms.py
from django import forms
from .models import HireMe

class HireMeForm(forms.ModelForm):
    class Meta:
        model = HireMe
        fields = ['company_name', 'salary_offering', 'bond', 'bond_duration_years', 'your_name', 'contact_no', 'email_id']
        widgets = {
            'bond': forms.CheckboxInput(),
            'bond_duration_years': forms.NumberInput(attrs={'placeholder': 'If yes, how many years?'}),
        }
