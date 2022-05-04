from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class NewuserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model=User
        fields=['email', 'username', 'password1', 'password2']

    
    # def save(self, commit=True):
    #         user = super(NewuserForm, self).save(commit=False)
    #         user.email = self.cleaned_data['email']
    #         if commit:
    #             user.save()
    #         return user
