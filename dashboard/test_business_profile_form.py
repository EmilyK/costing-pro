from forms import BusinessProfileForm
from django.test import TestCase

#check whether the form exists
#check whether form has the right number of fields
#check whether form has been saved


class BusinessProfileFormTest(TestCase):

	def test_should_check_that_form_exists(self):
		fields= {
		'business_name': 'craftsshop', 
		'city': 'Kampala',
		'division': 'Kawempe',
		'parish': 'makindye',
		'village': 'nakawa',
		'category': 'CRAFTS',
		'telephone_number': '0776787890'
		}
		form = BusinessProfileForm(data= fields)
		form.is_valid()
		print form.errors
		self.assertTrue(form.is_valid())
		craftsprofile = form.save()
		self.assertEqual(craftsprofile.business_name, fields['business_name'])
		self.assertEqual(craftsprofile.telephone_number, fields['telephone_number'])




