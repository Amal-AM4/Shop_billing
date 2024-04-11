import uuid
from django.db import models

# Create your models here.
class CustomerTable(models.Model):
    c_id =models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=50)
    vat_no = models.CharField(max_length=50)
    cr_no = models.CharField(max_length=50)
    address = models.TextField()
    phone = models.CharField(max_length=13, unique=True)
    email = models.EmailField(max_length=100)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'CustomerTable'

    def __str__(self):
        return str(self.name)