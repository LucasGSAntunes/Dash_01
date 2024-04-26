from django.forms import ModelForm
from Dash.models import User

class userForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']