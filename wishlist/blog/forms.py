from django import forms

class BlogForm(forms.Form):
    STATUS_CHOICES = (
        ('To be done', 'To be done'),
        ('Achieved', 'Achieved'),
        ('Dreaming', 'Dreaming'),
        ('Abandon', 'Abandon'),
    )

    title = forms.CharField(max_length=255)
    body_text = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 10}))
    image = forms.ImageField(required=False)
    status = forms.ChoiceField(choices=STATUS_CHOICES)
    #status = forms.ChoiceField(widget=forms.RadioSelect,choices=STATUS_CHOICES)
