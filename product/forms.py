from django import forms
from .models import ProductTable

class ProductTableForm(forms.ModelForm):
    
    class Meta:
        model = ProductTable
        fields = '__all__'
