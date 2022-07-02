from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField('Foto de perfil', upload_to = 'profile-image', null=True, blank=True)
    description = models.CharField('Descripción:', max_length=255, null=True, blank=True)
    phone = models.CharField('Número de teléfono:', max_length=15,null=True, blank=True)

class userAddresses(models.Model):
    def __str__(self):
        nombre = str(self.street) + ' ' + str(self.number) + ' ' + str(self.city)
        return (nombre)

    user = models.ForeignKey(User, related_name='addresses', on_delete=models.CASCADE)
    street = models.CharField('Calle:', max_length=255)
    number = models.IntegerField('Numero:')
    flat = models.CharField('Piso:', max_length=255, blank=True, null=True)
    apartment = models.CharField('Dpto:', max_length=255, blank=True, null=True)
    city = models.CharField('Ciudad:', max_length=255)
    province = models.CharField('Provincia:', max_length=255)
    additionalInfo = models.TextField('Info Adicional:', blank=True, null=True)
    code = models.CharField('CP:', max_length=8)

    class Meta:
        verbose_name = 'Dirección'
        verbose_name_plural = 'Direcciones'


