from django import forms
from .models import Message


class ContactForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control', 'placeholder':'Email', 'required': True}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Subject', 'required': True}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'placeholder':'Message', 'required': True}))
    # message = forms.CharField()

    class Meta:
        model = Message
        fields = ('email', 'subject', 'message',)