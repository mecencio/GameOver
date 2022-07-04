from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class cancelRequest(models.Model):
    STATUS_CHOICES = [
        ('Pedido ingresado', 'Pedido ingresado'),
        ('En gestión', 'En gestión'),
        ('Cancelación realizada', 'Cancelación realizada'),
        ('Cancelación rechazada', 'Cancelación rechazada'),
    ]

    user = models.ForeignKey(User, related_name='cancelOrder', on_delete=models.CASCADE)
    name = models.CharField('Nombre:', max_length=255)
    email = models.EmailField('Email:')
    phone = models.CharField('Número de teléfono:', max_length=30)
    order = models.CharField('Orden:', max_length=255)
    description = models.CharField('Descripción:', max_length=255)
    cancel_date = models.DateTimeField('Fecha de pedido de cancelación:', auto_now_add=True)

    status = models.CharField('Estado:', max_length=25, choices=STATUS_CHOICES, default='Pedido ingresado')

class messagesContactUs(models.Model):
    subject = models.CharField('Asunto:', max_length=255)
    email = models.EmailField('Email:')
    message = models.CharField('Mensaje:', max_length=255)