from django import forms

class SearchForm(forms.Form):
    city = forms.CharField(max_length=100, label='City', widget=forms.TextInput(attrs={
        'placeholder': 'Enter city name',
        'class': 'form-control',
    }))
