from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=20)
    image = models.FileField(upload_to='profile_picture')
    slug = AutoSlugField(populate_from = "name")

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name