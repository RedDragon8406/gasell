from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import os


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    user = User.objects.get(id=instance.id)
    final_name = f"{instance.id}-{user.username}{ext}"
    print(f'instance id : {instance.id}')
    return f"accounts/{final_name}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name='یوزر')
    pfp = models.ImageField(upload_to=upload_image_path,default="./accounts/default_pfp.jpeg",verbose_name='تصویر')

    class Meta:
        verbose_name="پروفایل"
        verbose_name_plural="پروفایل ها"

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()