from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from user.models import CustomUser

from allauth.account.forms import SignupForm
from allauth.account.forms import SignupForm

class MyCustomSignupForm(SignupForm):

    def __init__(self):
        self.email = forms.EmailField(required=True,)
        self.nameUser = forms.CharField(max_length=80,required=True,)
        self.password1 = forms.CharField(widget=forms.PasswordInput)
        self.password2 = forms.CharField(widget=forms.PasswordInput)

    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user

    class Meta:
        model = get_user_model()
        fields = ['username','nameUser','email','phone_number','gender']


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'email','phone_number','gender','nameUser']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email','phone_number','gender', 'nameUser']
