import uuid
from django.db import models
from customer.models import CustomerTable
from product.models import ProductTable


# Create your models here.
class SalesTable (models.Model):
    sale_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    customer = models.ForeignKey(CustomerTable, on_delete=models.CASCADE)
    doc_no = models.CharField( max_length=50)
    sales_man = models.CharField( max_length=100)
    total_taxable_amount = models.DecimalField( max_digits=10, decimal_places=2, default=0)
    total_tax_amount = models.DecimalField( max_digits=10, decimal_places=2, default=0)
    total_disc_amount = models.DecimalField( max_digits=10, decimal_places=2, default=0)
    total_grand_total = models.DecimalField( max_digits=10, decimal_places=2, default=0)
    # created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'SalesTable'

class SaleItemTable (models.Model):
    sale_item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    sales = models.ForeignKey(SalesTable, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductTable, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.CharField(default=15)
    discount = models.CharField( max_length=15)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'SaleItemTable'
