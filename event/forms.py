from django import forms

class EmailForm(forms.Form):
    receiver_mail = forms.EmailField(label="enter email id")
    subject = forms.CharField(max_length=255, label= "Enter Subject")
    email_text = forms.CharField(widget=forms. Textarea, label= "Enter Email Text")
