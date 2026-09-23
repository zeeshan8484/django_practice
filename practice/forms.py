from django import forms
# creating a form class to handle the user input
class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()