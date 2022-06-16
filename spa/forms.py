from django.forms import ModelForm
from .models import User

class UserForm(ModelForm):
    class meta:
        model = User
        fields = '__all__'
