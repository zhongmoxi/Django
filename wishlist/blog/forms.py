from django import forms

class BlogForm(forms.Form):
    title = forms.CharField(max_length=255)
    # body_text = forms.CharField(widget=forms.Textarea)
    body_text = forms.CharField(max_length=255)
    image = forms.ImageField(required=False)  
