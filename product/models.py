import uuid
from django.db import models

# Create your models here.
class ProductTable (models.Model):
    p_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=10)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    selling_price = models.DecimalField(max_digits=8, decimal_places=2)
    unit = models.IntegerField()
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'ProductTable'

    def __str__(self):
        return str(self.name)


