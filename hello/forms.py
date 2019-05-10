from django import forms

class HelloForm(forms.Form):
    date = forms.CharField(label = 'date')