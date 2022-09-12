from django.db import models
from apps.authentication.models import User
from django.utils.translation import gettext_lazy as _


# For storing product details.
class Product(models.Model):
    class UnitChoices(models.TextChoices):
        KILOGRAM = 'kg', _('KILOGRAM')
        POUND = 'lbs', _('POUND')
        Ounce = 'oz', _('Ounce')

    product_id = models.AutoField(primary_key=True)
    name = models.TextField()
    # quantity = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to='products/', default='products/no_image.png', null=True,
                                      blank=True)
    status = models.PositiveSmallIntegerField(default=2)
    length = models.FloatField(default=0.0)
    width = models.FloatField(default=0.0)
    height = models.FloatField(default=0.0)
    weight = models.FloatField(default=0.0)
    weight_unit = models.CharField(
        max_length=3,
        choices=UnitChoices.choices,
        default=UnitChoices.KILOGRAM,
    )
    description = models.TextField(blank=True, null=True)

    modified_datetime = models.DateTimeField(auto_now=True, blank=True, null=True)
    modified_date = models.DateField(auto_now=True, blank=True, null=True)
    created_datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'


# For storing warehouse details.
class Warehouse(models.Model):
    warehouse_id = models.AutoField(primary_key=True)
    name = models.TextField()
    state = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, related_name='warehouse_owner_fk', null=True, blank=True,
                              on_delete=models.PROTECT)

    warehouse_image = models.ImageField(upload_to='media/warehouse/', default='media/warehouse/no_image.png', null=True,
                                        blank=True)

    modified_datetime = models.DateTimeField(auto_now=True, blank=True, null=True)
    modified_date = models.DateField(auto_now=True, blank=True, null=True)
    created_datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'warehouse'


# For storing product charges for warehouse specific details.
class ChargesPerWarehouse(models.Model):
    charges_per_warehouse_id = models.AutoField(primary_key=True)

    product_id = models.ForeignKey(Product, related_name='charges_per_warehouse_product_fk', null=True, blank=True,
                                   on_delete=models.PROTECT)
    warehouse_id = models.ForeignKey(Warehouse, related_name='charges_per_warehouse_warehouse_fk', null=True,
                                     blank=True,
                                     on_delete=models.PROTECT)

    prep_charges = models.FloatField(default=0.0)
    pickup_charges = models.FloatField(default=0.0)
    shipping_charges = models.FloatField(default=0.0)

    modified_datetime = models.DateTimeField(auto_now=True, blank=True, null=True)
    modified_date = models.DateField(auto_now=True, blank=True, null=True)
    created_datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.product_id + "_" + self.warehouse_id

    class Meta:
        db_table = 'charges_per_warehouse'
