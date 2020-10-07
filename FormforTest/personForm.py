from django.forms import ModelForm
from .models import from_details


class PersonForm(ModelForm):
    class Meta:
        model = from_details
        fields = ['fname', 'lname', 'email', 'degree', 'education', 'address']
