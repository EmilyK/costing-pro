from django.db import models
from django.contrib.auth.models import User

# Create your models here
class BusinessProfile(models.Model):
	CATEGORIES = (('CRAFTS', 'Crafts'),)

	business_name= models.CharField(max_length=100, blank=False)
	city= models.CharField(max_length=30)
	division= models.CharField(max_length=20)
	parish=models.CharField(max_length=20)
	village= models.CharField(max_length=20)
	category = models.CharField(max_length=15, choices=CATEGORIES)
	telephone_number = models.CharField(max_length=10, blank=False)
	user = models.ForeignKey(User, null=True)

	def __unicode__(self):
		return self.business_name

class RawMaterial(models.Model):
	time_rate = models.CharField(max_length=50, choices=(('d', 'daily'), 
		                         ('w', 'weekly'),
		                         ('m', 'monthly')))
	name = models.CharField(max_length=50)
	size = models.DecimalField(max_digits=10, default=0.00, decimal_places=3)
	cost = models.DecimalField(max_digits=50, default=0.00, decimal_places=5)
	business_profile = models.ForeignKey(BusinessProfile, null=True, blank=True)

	def __unicode__(self):
		return self.name