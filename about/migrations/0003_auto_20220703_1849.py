# Generated by Django 3.2.6 on 2022-07-03 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_alter_cancelrequest_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancelrequest',
            name='cancel_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de pedido de cancelación:'),
        ),
        migrations.AddField(
            model_name='cancelrequest',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha del pedido:'),
        ),
        migrations.AddField(
            model_name='cancelrequest',
            name='status',
            field=models.CharField(choices=[('Pedido ingresado', 'Pedido ingresado'), ('En gestión', 'En gestión'), ('Cancelación realizada', 'Cancelación realizada'), ('Cancelación rechazada', 'Cancelación rechazada')], default='Pedido ingresado', max_length=25, null=True, verbose_name='Estado:'),
        ),
        migrations.AlterField(
            model_name='cancelrequest',
            name='phone',
            field=models.CharField(max_length=30, verbose_name='Número de teléfono:'),
        ),
    ]