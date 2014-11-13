from django.db import models

# Create your models here.
class BusinessProfile(models.Model):
	CATEGORIES = (('CRAFTS', 'Crafts'),)

	business_name= models.CharField(max_length=100, blank=False)
	city= models.CharField(max_length=30)
	division= models.CharField(max_length=20)
	parish=models.CharField(max_length=20)
	village= models.CharField(max_length=20)
	category = models.CharField(max_length=15, choices=CATEGORIES)
	telephone_number = models.IntegerField(max_length=10, blank=False)

