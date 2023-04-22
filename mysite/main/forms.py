from django  import forms
from .models import MyUser


class MyUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['user_name', 'user_password']