from django import forms
from models import BusinessProfile, RawMaterial
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

class UpdateProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

    def save(self, commit=True):
        user = super(UserSignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user