from django import forms
from django.contrib.auth.models import User
from .models import Company
class SignupForm(forms.Form):
    company = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'company name', 'class' : 'form-control' }), required=False)
    email = forms.EmailField(max_length=255, label="Email")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-4', 'placeholder':'input your password' }), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-4', 'placeholder':'input your password' }), label="Password (again)")
    last_name = forms.CharField(max_length=60, label='Last Name', widget=forms.TextInput(attrs={'placeholder':'First Name', 'class':'form-control col-6' }), required=False)
    first_name = forms.CharField(max_length=60, label='First Name', widget=forms.TextInput(attrs={'placeholder':'First Name', 'class':'form-control col-6' }), required=False)

 
    def signup(self, request, user):
        user.company.name = self.cleaned_data['company']
        user.last_name = self.cleaned_data['last_name']
        user.first_name = self.cleaned_data['first_name']
        user.save()
    
    class Meta:
        model = User
        fields = ('email', 'password', )

class ProfileUploadForm(forms.Form):
    
    img = forms.FileField(widget=forms.ClearableFileInput(attrs={'placeholder':'input your password', 'class': 'custom-file-input',  'oninput' : 'input_filename();',  }))