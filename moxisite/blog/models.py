from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    body_text = models.CharField(max_length=1024)
    #img = models.FileField()
    #pub_date = models.DateTimeField()
    #authors = models.CharField()

    def __unicode__(self):
        return self.title
