from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class Webstaapp(models.Model):
    writer = models.ForeignKey(User, related_name="post", on_delete=CASCADE)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
