from models import BusinessProfile 
from django.test import TestCase

class BusinessProfileTest(TestCase):
	def test_bussiness_profile_has_all_fields_listed(self):
		business_profile = BusinessProfile()

		fields =['business_name', 'category', 'city', 'division', 'village', 'parish', 'telephone_number']

		for field in fields:
			self.assertTrue(hasattr(business_profile,field))
		#the len is 8 because django auto adds id for each model	
		self.assertEqual(8, len(business_profile._meta.fields))

	