from django import forms

class FactorForm(forms.Form):
    factor_id = forms.CharField(max_length=100)
    sentiment = forms.CharField(max_length=7)

