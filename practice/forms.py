from django import forms


# creating a form class to handle the user input
class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()


class MarksheetForm(forms.Form):
    student_name = forms.CharField(max_length=100)
    roll_number = forms.CharField(max_length=20)
    math = forms.IntegerField(min_value=0, max_value=100)
    science = forms.IntegerField(min_value=0, max_value=100)
    english = forms.IntegerField(min_value=0, max_value=100)
    computer = forms.IntegerField(min_value=0, max_value=100)