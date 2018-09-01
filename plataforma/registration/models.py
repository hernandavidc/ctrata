from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

#instance hace referencia al objeto que se esta guardando
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

PROFILE_CHOICES = (
		('o', 'Operario'), 
		('e', 'Entidad'), 
	)

class Pais(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"
        ordering = ['-created']

    def __str__(self):
        return self.name

class Ciudad(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        ordering = ['-created']

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    ciudad = models.ForeignKey(Ciudad, null=True, blank=True, on_delete=models.CASCADE)
    typeProfile = models.CharField(choices=PROFILE_CHOICES, max_length=1, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    dni = models.PositiveIntegerField(unique=True)

    class Meta:
        ordering = ['user__username']

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)


