from django import forms

class BlogForm(forms.Form):
    title = forms.CharField(max_length=255)
    body_text = forms.CharField(widget=forms.Textarea)
    img = forms.FileField()
