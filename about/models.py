from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class cancelRequest(models.Model):
    user = models.ForeignKey(User, related_name='cancelOrder', on_delete=models.CASCADE)
    name = models.CharField('Nombre:', max_length=255)
    email = models.EmailField('Email:')
    phone = models.CharField('Número de teléfono:', max_length=30)
    order = models.CharField('Orden:', max_length=255)
    description = models.CharField('Descripción:', max_length=255)
    cancel_date = models.DateTimeField('Fecha de pedido de cancelación:', auto_now_add=True)

    status = models.CharField('Estado:', max_length=25, default='Pedido ingresado')

    response = models.CharField('Respuesta:', max_length=255, null=True)
    employee = models.CharField('Empleado:', max_length=255, null=True, default='-')

    class Meta:
        verbose_name = 'Pedido de cancelación'
        verbose_name_plural = 'Pedidos de cancelación'

    def __str__(self):
        return self.name

class messagesContactUs(models.Model):
    subject = models.CharField('Asunto:', max_length=255)
    email = models.EmailField('Email:')
    message = models.CharField('Mensaje:', max_length=255)

    status = models.CharField('Estado:', max_length=25, default='Sin ver')

    response = models.CharField('Respuesta:', max_length=255, null=True)
    employee = models.CharField('Empleado:', max_length=255, null=True, default='-')

    class Meta:
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'

    def __str__(self):
        return self.subject