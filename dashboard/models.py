from django.db import models
from exceptions import ZeroDivisionError
from django.contrib.auth.models import User


# Create your models here
class BusinessProfile(models.Model):
    CATEGORIES = (('CRAFTS', 'Crafts'),)
    business_name = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=30)
    division = models.CharField(max_length=20)
    parish = models.CharField(max_length=20)
    village = models.CharField(max_length=20)
    category = models.CharField(max_length=15, choices=CATEGORIES)
    telephone_number = models.CharField(max_length=10, blank=False)
    user = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return self.business_name


class RawMaterial(models.Model):
    time_rate = models.CharField(max_length=50, choices=(('d', 'Daily'),
        ('w', 'Weekly'),
        ('m', 'Monthly')))
    name = models.CharField(max_length=50)
    original_size = models.DecimalField(max_digits=10, default=0.00, decimal_places=3)
    size = models.DecimalField(max_digits=10, default=0.00, decimal_places=3)
    cost = models.DecimalField(max_digits=50, default=0.00, decimal_places=5)
    business_profile = models.ForeignKey(BusinessProfile, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Product(models.Model):
	name = models.CharField(max_length=50, verbose_name='Product name')
	product_size = models.CharField(max_length = 8, choices=(('s', 'Small'), ('m', 'Medium'),
									('l', 'Large')))
	business_profile = models.ForeignKey(BusinessProfile, null=True, blank=True)

	# State depicts whether product has been fully created with RawMaterials
	created = models.BooleanField(default=False)
	
	def __unicode__(self):
		return "{0} ({1})".format(self.name, self.product_size.upper())



class ProductRawMaterial(models.Model):
    raw_material = models.ForeignKey(RawMaterial)
    product = models.ForeignKey(Product)
    amount = models.IntegerField(default=1)
    business_profile = models.ForeignKey(BusinessProfile, null=True, blank=True)

    def get_estimated_unit_price(self):
        try:
            return (self.amount/self.raw_material.original_size) * self.raw_material.cost
        except ZeroDivisionError:
            return "Raw Materials not in stock!"
