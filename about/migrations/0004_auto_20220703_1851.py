# Generated by Django 3.2.6 on 2022-07-03 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20220703_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancelrequest',
            name='cancel_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de pedido de cancelación:'),
        ),
        migrations.AlterField(
            model_name='cancelrequest',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha del pedido:'),
        ),
        migrations.AlterField(
            model_name='cancelrequest',
            name='status',
            field=models.CharField(choices=[('Pedido ingresado', 'Pedido ingresado'), ('En gestión', 'En gestión'), ('Cancelación realizada', 'Cancelación realizada'), ('Cancelación rechazada', 'Cancelación rechazada')], default='Pedido ingresado', max_length=25, verbose_name='Estado:'),
        ),
    ]