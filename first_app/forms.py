from django import forms
from django.core import validators
from first_app.models import User


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email= forms.EmailField(label="Enter your email again")
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verify_email = all_clean_data['verify_email']
        if(email != verify_email):
            raise forms.ValidationError('Email dosn\'t match')


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'