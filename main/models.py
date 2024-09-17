import uuid
from django.db import models

class ProductEntry(models.Model):
    id = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=255)
    product_price = models.IntegerField()
    product_description = models.TextField()
# Create your models here.
    @property
    def is_product_expensive(self):
        return self.product_price> 100000
