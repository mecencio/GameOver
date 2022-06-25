from django.contrib.auth.models import User
from django.db import models
from products.models import Products

# Create your models here.
class Order(models.Model):
    def __str__(self):
        nombre = self.client_name + ' - Orden: ' + str(self.id)
        return (nombre)

    STATUS_CHOICES = [
        ('Pedido ingresado', 'Pedido ingresado'),
        ('Componentes reservados', 'Componentes reservados'),
        ('Armada', 'Armada'),
        ('Enviada', 'Enviada'),
        ('Recibida', 'Recibida'),
    ]

    PROVINCE_CHOICES = [
        ('Buenos Aires', 'Buenos Aires'),
        ('Ciudad Autónoma de Buenos Aires', 'Ciudad Autónoma de Buenos Aires'),
        ('Catamarca', 'Catamarca'),
        ('Chaco', 'Chaco'),
        ('Chubut', 'Chubut'),
        ('Córdoba', 'Córdoba'),
        ('Corrientes', 'Corrientes'),
        ('Entre Ríos', 'Entre Ríos'),
        ('Formosa', 'Formosa'),
        ('Jujuy', 'Jujuy'),
        ('La Pampa', 'La Pampa'),
        ('La Rioja', 'La Rioja'),
        ('Mendoza', 'Mendoza'),
        ('Misiones', 'Misiones'),
        ('Neuquén', 'Neuquén'),
        ('Río Negro', 'Río Negro'),
        ('Salta', 'Salta'),
        ('San Juan', 'San Juan'),
        ('San Luis', 'San Luis'),
        ('Santa Cruz', 'Santa Cruz'),
        ('Santa Fe', 'Santa Fe'),
        ('Santiago del Estero', 'Santiago del Estero'),
        ('Tierra del Fuego', 'Tierra del Fuego'),
        ('Tucumán', 'Tucumán'),
    ]

    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    street = models.CharField(max_length=255)
    number = models.IntegerField()
    flat = models.CharField(max_length=255, blank=True, null=True)
    apartment = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255, choices=PROVINCE_CHOICES)
    code = models.CharField(max_length=8)
    phone = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(blank=True, null=True)

    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='Pedido ingresado')

    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'


class OrderItems(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField()