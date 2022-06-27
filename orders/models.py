from django.contrib.auth.models import User
from django.db import models
from products.models import Products

# Create your models here.
class Order(models.Model):
    def __str__(self):

        nombre = self.first_name + ' ' + self.last_name + ' - Orden: ' + str(self.id)
        return (nombre)

    STATUS_CHOICES = [
        ('Pedido ingresado', 'Pedido ingresado'),
        ('Componentes reservados', 'Componentes reservados'),
        ('Armada', 'Armada'),
        ('Enviada', 'Enviada'),
        ('Recibida', 'Recibida'),
    ]

    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    first_name = models.CharField('Nombre:', max_length=255)
    last_name = models.CharField('Apellido:', max_length=255)
    email = models.EmailField('Email:')
    street = models.CharField('Calle:', max_length=255)
    number = models.IntegerField('Numero:')
    flat = models.CharField('Piso:', max_length=255, blank=True, null=True)
    apartment = models.CharField('Dpto:', max_length=255, blank=True, null=True)
    city = models.CharField('Ciudad:', max_length=255)
    province = models.CharField('Provincia:', max_length=255)
    additionalInfo = models.TextField('Info Adicional:')
    code = models.CharField('CP:', max_length=8)
    phone = models.IntegerField('Telefono:', )
    create_at = models.DateTimeField('Pedido el:', auto_now_add=True)

    paid = models.BooleanField('Pago', default=False)
    paid_amount = models.IntegerField('Monto:', blank=True, null=True)

    status = models.CharField('Estado:', max_length=25, choices=STATUS_CHOICES, default='Pedido ingresado')

    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'


class OrderItems(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField('Precio:')
    quantity = models.IntegerField('Cantidad:', default=1)
    total_price = models.IntegerField('Precio total:')