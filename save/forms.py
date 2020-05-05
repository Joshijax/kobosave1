from django import forms
from django.contrib.auth.models import User
from .models import Company
from allauth.account.forms import LoginForm
from allauth.account import app_settings
from allauth.account.adapter import get_adapter
from allauth.account.app_settings import AuthenticationMethod
from allauth.utils import (
    build_absolute_uri,
    get_username_max_length,
    set_form_field_order,
)

class SignupForm(forms.Form):
    company = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'company name', 'class' : 'form-control' }), required=False)
    email = forms.EmailField(max_length=255, label="Email", widget=forms.TextInput(
        attrs={'type': 'email', 'class':'form-control mb-4',
               'placeholder': 'E-mail address'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-4', 'placeholder':'input your password' }), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-4', 'placeholder':'input your password' }), label="Password (again)")
    last_name = forms.CharField(max_length=60, label='Last Name', widget=forms.TextInput(attrs={'placeholder':'Last Name', 'class':'form-control col-6' }), required=False)
    first_name = forms.CharField(max_length=60, label='First Name', widget=forms.TextInput(attrs={'placeholder':'First Name', 'class':'form-control col-6' }), required=False)

 
    def signup(self, request, user):
        user.company.name = self.cleaned_data['company']
        user.last_name = self.cleaned_data['last_name']
        user.first_name = self.cleaned_data['first_name']
        user.save()
    
    class Meta:
        model = User
        fields = ('email', 'password', )

class LoginForm(LoginForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password', 'class':'form-control mb-4', 'placeholder':'password',}))
    login = forms.EmailField(max_length=255, label="Email", widget=forms.TextInput(
        attrs={'type': 'email', 'class':'form-control mb-4',
               'placeholder': ('E-mail addresss')}))
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)
        if app_settings.AUTHENTICATION_METHOD == AuthenticationMethod.EMAIL:
            login_widget = forms.TextInput(attrs={'type': 'email', 'class':'form-control mb-4',
                                                  'placeholder':
                                                  ('E-mail addresss'),
                                                  'autofocus': 'autofocus'})
            login_field = forms.EmailField(label=("E-mail"),
                                           widget=login_widget)
        elif app_settings.AUTHENTICATION_METHOD \
                == AuthenticationMethod.USERNAME:
            login_widget = forms.TextInput(attrs={'placeholder':
                                                  _('Username'),
                                                  'autofocus': 'autofocus'})
            login_field = forms.CharField(
                label=_("Username"),
                widget=login_widget,
                max_length=get_username_max_length())
        else:
            assert app_settings.AUTHENTICATION_METHOD \
                == AuthenticationMethod.USERNAME_EMAIL
            login_widget = forms.TextInput(attrs={'placeholder':
                                                  _('Username or e-mail'),
                                                  'autofocus': 'autofocus'})
            login_field = forms.CharField(label=pgettext("field label",
                                                         "Login"),
                                          widget=login_widget)
        self.fields["login"] = login_field
        set_form_field_order(self, ["login", "password", "remember"])
        if app_settings.SESSION_REMEMBER is not None:
            del self.fields['remember']
    

class ProfileUploadForm(forms.Form):
    
    img = forms.FileField(widget=forms.ClearableFileInput(attrs={'placeholder':'input your password', 'class': 'custom-file-input',  'oninput' : 'input_filename();',  }))