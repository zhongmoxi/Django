from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime



class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('Female', 'Female'),
        ('male', 'male'),
    )
    user = models.OneToOneField(User)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, default='Female')
    bio = models.CharField(max_length=255)
    url_token = models.CharField(max_length=255)
    birthday = models.DateField(default=datetime.datetime.now().date())
    portrait = models.ImageField(upload_to='photos/user/', blank=True, null=True)

    def __unicode__(self):
        return self.user.username


STATUS_CHOICES = (
        ('To be done', 'To be done'),
        ('Achieved', 'Achieved'),
        ('Dreaming', 'Dreaming'),
        ('Abandon', 'Abandon'),
)

class Blog(models.Model):
    title = models.CharField(max_length=255)
    body_text = models.CharField(max_length=1024)
    image = models.ImageField(upload_to='photos', blank=True, null=True)
    #author = models.CharField(max_length=255)
    author = models.ForeignKey(UserProfile)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='To be done')
    publish_time = models.DateTimeField(auto_now_add=True)
    expected_date = models.DateField(default=datetime.datetime.now().date()+datetime.timedelta(days=100))
    privacy = models.NullBooleanField()

    def __unicode__(self):
        return self.title



def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
