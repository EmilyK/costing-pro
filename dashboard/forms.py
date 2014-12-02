from django import forms
from models import BusinessProfile, RawMaterial, Product
from django.contrib.auth.models import User


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
        
class UserSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email', 
            'password'
            )


class RawmaterialForm(forms.ModelForm):

    class Meta:
        model = RawMaterial
        fields = (
            'time_rate',
            'name'
            )

