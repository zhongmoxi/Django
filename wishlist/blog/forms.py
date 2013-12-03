from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm, Textarea
from blog.models import Blog


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        exclude = ('author',)
        widgets = {
            'body_text': Textarea(attrs={'cols': 10, 'rows': 10}),
        }

class UserForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)