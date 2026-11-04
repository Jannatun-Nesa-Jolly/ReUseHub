from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ItemListing, Report, Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ListingForm(forms.ModelForm):
    class Meta:
        model = ItemListing
        fields = ('title', 'category', 'description', 'condition', 'listing_type', 'price', 'image')
        widgets = {'description': forms.Textarea(attrs={'rows': 4})}

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('reason',)
        widgets = {'reason': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Tell the admin what seems wrong...'})}

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('display_name', 'contact_preference')
