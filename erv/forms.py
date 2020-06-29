from django import forms

class ArticleMappingForm(forms.Form):
    article = forms.CharField(max_length=100)
    