from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save, post_delete, post_init
from django.dispatch import receiver
from django.conf import settings
import os
# Create your models here.
class Company(models.Model):
    user = models.OneToOneField(User, related_name="company", on_delete=models.CASCADE,)
    name = models.CharField(max_length = 100)


class ProfilPicx(models.Model):
    user = models.OneToOneField(User, related_name="profilePicx", on_delete=models.CASCADE,)
    
    img = models.FileField(upload_to = '', null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.img:
            self.img = 'U'
        return super().save(*args, **kwargs)
    def delete(self, *args, **kwargs):
        if os.path.join(settings.MEDIA_ROOT, self.img.name) == os.path.join(settings.MEDIA_ROOT, 'U'):
            return True
        else:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.img.name))
        


@receiver(post_save, sender= settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Company.objects.create(user=instance)
        ProfilPicx.objects.create(user=instance)
