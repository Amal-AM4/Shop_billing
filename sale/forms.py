from django import forms
from .models import SalesTable, SaleItemTable
from product.models import ProductTable

class SalesTableForm(forms.ModelForm):
    doc_no = forms.CharField(
        initial='DOC/23/01'
    )
    CHOICES = [
        ('Counter 1', 'Counter 1'),
        ('Counter 2', 'Counter 2'),
        ('Counter 3', 'Counter 3')
    ]
    sales_man = forms.ChoiceField( choices=CHOICES, required=False)
    
    class Meta:
        model = SalesTable
        # fields = '__all__'
        exclude = ['is_deleted', 'total_taxable_amount','total_tax_amount','total_disc_amount', 'created_at', 'total_grand_total']


class SaleItemTableForm(forms.ModelForm):

    add_button = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'btn btn-danger',
            'type': 'button',
            'value': '+',
            'name':'add_button',
            'id': 'add-item-btn',
            # 'onclick': 'addRowtoTable();',
            }),
        required=False  # Set this to False to prevent it from being validated
    )

    qty = forms.CharField(
        widget=forms.NumberInput(attrs={'value': '1', 'class': 'form-control'}
    ))
    total_price = forms.CharField(
        widget=forms.TextInput(attrs={ 'class': 'form-control'}
    ))
    tax = forms.CharField(
        widget=forms.TextInput(attrs={ 'value': '15', 'class': 'form-control'}
    ))

   


    class Meta:
        model = SaleItemTable
        exclude = ['is_deleted','sales']

        widgets = {
            'product': forms.Select(attrs={'class':'form-control', 'id': 'id_product'}),
            'discount': forms.TextInput(attrs={'class':'form-control', },),
            'tax_amount': forms.TextInput(attrs={'class':'form-control', },),
            'subtotal': forms.TextInput(attrs={'class':'form-control', },),
        }

    # Define the queryset for the product field
    product = forms.ModelChoiceField(
        queryset=ProductTable.objects.exclude(unit=0),
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_product'}),
    )

        
    




