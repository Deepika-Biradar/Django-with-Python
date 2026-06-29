
from django import forms
class EmailForm(forms.Form):
    receiver_mail = forms.EmailField(label="Enter email id")
    subject = forms.CharField(max_length=255, initial="Welcome to QuickNews/Notes! Confirmation for your Registration", widget=forms. TextInput(attrs={'readonly':'readonly'}), label= "Enter Subject")
    email_text = forms.CharField(initial="We're thrilled to welcome you to QuickNews/Notes! Your Registration is now confirmed, Now you can enjoy News instantly from anywhere, anytime. Thanking You, QuickNews/Notes ", widget=forms. Textarea(attrs={'readonly':'readonly'}), label= "Enter Email Text")