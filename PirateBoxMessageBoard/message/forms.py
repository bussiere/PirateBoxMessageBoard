from django import forms

class MessageForm(forms.Form):
    Pseudo = forms.CharField(max_length=100)
    Description = forms.CharField(max_length=100)
    Message = forms.CharField(widget=forms.Textarea(attrs={'cols': 20, 'rows': 20}))
