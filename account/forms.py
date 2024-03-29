from django import forms
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User

class FormSettings(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSettings, self).__init__(*args, **kwargs)
        # Here make some changes such as:
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'border w-full px-2 py-2 focus:outline-none focus:ring-0 text-base focus:border-gray-600'})
        self.fields['first_name'].widget.attrs.update({'class': 'border w-full px-2 py-2 focus:outline-none focus:ring-0 text-base focus:border-gray-600'})
        self.fields['last_name'].widget.attrs.update({'class': 'border w-full px-2 py-2 focus:outline-none focus:ring-0 text-base focus:border-gray-600'})
        self.fields['email'].widget.attrs.update({'class': 'border w-full px-2 py-2 focus:outline-none focus:ring-0 text-base focus:border-gray-600'})
        self.fields['password1'].widget.attrs.update({'class': 'border w-full px-2 py-2 focus:outline-none focus:ring-0 text-base focus:border-gray-600'})
        self.fields['password2'].widget.attrs.update({'class': 'border w-full px-2 py-2 focus:outline-none focus:ring-0 text-base focus:border-gray-600'})