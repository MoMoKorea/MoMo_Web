from django import forms
from .models import CustomUser

from datetime import timedelta
from django import forms
from django.forms import ValidationError
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils import timezone
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

# -----------------------------
#from django import forms
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

# ------------------------------


'''
class SignInViaEmailForm(SignIn):
    email = forms.EmailField(label=_('Email'))

    @property
    def field_order(self):
        if settings.USE_REMEMBER_ME:
            return ['email', 'password', 'remember_me']
        return ['email', 'password']

    def clean_email(self):
        email = self.cleaned_data['email'] ## email

        user = User.objects.filter(email__iexact=email).first()
        if not user:
            raise ValidationError(_('You entered an invalid email address.'))

        if not user.is_active:
            raise ValidationError(_('This account is not active.'))

        self.user_cache = user

        return email

class PostForm(forms.ModelForm): #forms의 ModelForm 클래스를 상속 받는다.

    class Meta:
        model = GuessNumbers #GuessNumbers와 연결
        fields = ('name', 'text', 'num_lotto', ) # 그 중에 입력 받을 것
'''
