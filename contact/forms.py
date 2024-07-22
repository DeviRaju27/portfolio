from django import forms

class ContactForm(forms.Form):
    name= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'your email'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'your message'}))