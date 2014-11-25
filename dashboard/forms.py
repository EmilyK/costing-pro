from django import forms
from models import BusinessProfile, UserSignUp, UserLogin, RawMaterial
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
        model = UserSignUp
        fields = (
            'firstname',
            'lastname',
            'username', 
            'password'
            )


class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserLogin
        fields = (
            'username',
            'password'
            )

class RawmaterialForm(forms.ModelForm):

    class Meta:
        model = RawMaterial
        fields = (
            'time_rate',
            'name'
            )