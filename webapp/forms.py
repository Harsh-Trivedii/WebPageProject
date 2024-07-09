from django import forms

class UserDataForm(forms.Form):
    name=forms.CharField(max_length=20)
    email=forms.EmailField()