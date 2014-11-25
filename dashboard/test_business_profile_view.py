from views import business_profile
from django.test import TestCase, Client

#render template
#template should have a form

class BusinessProfileViewTest(TestCase):

	def test_should_render_business_profile_template(self):
		client = Client()
		response = client.get('/business_profile/')
		
		self.assertEquals(200, response.status_code)
		self.assertTemplateUsed(response, 'dashboard/business_profile.html')

