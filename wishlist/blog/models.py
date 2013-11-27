from django.db import models


class Blog(models.Model):

    STATUS_CHOICES = (
        ('To be done', 'To be done'),
        ('Achieved', 'Achieved'),
        ('Dreaming', 'Dreaming'),
        ('Abandon', 'Abandon'),
    )

    title = models.CharField(max_length=255)
    body_text = models.CharField(max_length=1024)
    image = models.ImageField(upload_to='photos', blank=True, null=True)
    author = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='To be done')
    publish_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title
