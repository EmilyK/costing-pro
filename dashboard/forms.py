from django import forms
from models import BusinessProfile

class BusinessProfileForm(forms.ModelForm):


    class Meta:
        model = BusinessProfile
        fields = (
        	'business_name', 
        	'category',
			'city',
			'division',
			'parish',
			'village',
			'telephone_number'
        	)
        
    # def clean_business_name(self):
    # 	data = self.cleaned_data['business_name']

    # 	if 'business_name' is ('')

    # 		ValidationError: (('This field is required.'))
    	
