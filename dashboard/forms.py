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
    #TODO please hash the passwords for security
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
            'name',
            'size',
            'cost'
            )


class LoginForm(forms.Form):

    username= forms.CharField(required=True)
    password= forms.CharField(required=True, widget=forms.PasswordInput)

class ProductForm(forms.ModelForm):

    class Meta:
        model =  Product 
        exclude = ['business_profile', 'created', ]



class ProductRawMaterialForm(forms.Form):

    raw_material = forms.ChoiceField(label=u'Raw Material', required=True)
    amount=  forms.CharField(required=True)
    
    def __init__(self, business_profile, *args, **kwargs):
        super(ProductRawMaterialForm, self).__init__(*args, **kwargs)
        self.fields['raw_material'].choices = [
                                                (rm.id, rm.name) 
                                                for rm in RawMaterial.objects.filter(business_profile=business_profile)]
    