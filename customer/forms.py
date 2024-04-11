from django import forms
from .models import CustomerTable

class CustomerTableForm(forms.ModelForm):
    
    class Meta:
        model = CustomerTable
        fields = '__all__'
        exclude = ['vat_no', 'cr_no']
