from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Modelo de perfil extendido
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'

# Señal para crear perfil automáticamente al crear un usuario
@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# Agrega propiedad profile al modelo User
def get_profile(self):
    return UserProfile.objects.get_or_create(user=self)[0]

User.add_to_class('profile', property(get_profile))
