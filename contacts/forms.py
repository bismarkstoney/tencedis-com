from django import forms

class ContactForm(forms.Form):
    email=forms.EmailField(required=False)
    subject= forms.CharField(required=True)
    message=forms.CharField(widget=forms.Textarea)