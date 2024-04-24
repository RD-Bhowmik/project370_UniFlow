from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User, Group
from django import forms  

from .models  import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class ChangeUserGroupForm(forms.Form):
#     user = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
#     group = forms.ModelChoiceField(queryset=Group.objects.all())
#     new_group = forms.CharField(max_length=100, required=False)
#     action = forms.ChoiceField(choices=(('add', 'Add'), ('remove', 'Remove')))
        
class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['name', 'email', 'blood_type', 'phone_number', 'address']



class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['name', 'location', 'email']




class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'location', 'status']


# class BloodRequestForm(forms.ModelForm):
#     class Meta:
#         model = BloodRequest
#         fields = '__all__'


class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = ['name', 'address', 'blood_type', 'age', 'disease', 'need_within_date', 'phone_number', 'email']
        # fields = '__all__'


