from django import forms

class Createlist(forms.Form):
    name = forms.CharField(max_length=200, required=True)

class Createitemlist(forms.Form):
    text = forms.CharField(max_length=300,required=True  )
    
