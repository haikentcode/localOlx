from django import forms
from django.forms import ModelForm
from .models import User,Item



class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(metaForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'someClass'

# Create the form class.
class SignupForm(ModelForm):
   class Meta:
       model = User
       fields = ['firstName', 'lastName', 'emailId', 'contactNo','cityName','dateOfBirth','password']

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name','image','price','info','user','status','date']
