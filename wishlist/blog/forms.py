from django import forms
from django.forms.extras.widgets import SelectDateWidget

class BlogForm(forms.Form):
    STATUS_CHOICES = (
        ('To be done', 'To be done'),
        ('Achieved', 'Achieved'),
        ('Dreaming', 'Dreaming'),
        ('Abandon', 'Abandon'),
    )
    #BIRTH_YEAR_CHOICES = ('1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998')

    title = forms.CharField(max_length=255)
    body_text = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 10}))
    image = forms.ImageField(required=False)
    status = forms.ChoiceField(choices=STATUS_CHOICES)
    privacy = forms.NullBooleanField()
    #expected_date = forms.DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    #expected_date = forms.DateField(input_formats=['%Y/%m/%d'], widget=forms.DateInput(format = '%Y/%m/%d'))
    #status = forms.ChoiceField(widget=forms.RadioSelect,choices=STATUS_CHOICES)
