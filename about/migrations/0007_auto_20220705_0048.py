# Generated by Django 3.2.6 on 2022-07-05 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_messagescontactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancelrequest',
            name='employee',
            field=models.CharField(max_length=255, null=True, verbose_name='Respuesta:'),
        ),
        migrations.AddField(
            model_name='cancelrequest',
            name='response',
            field=models.CharField(max_length=255, null=True, verbose_name='Respuesta:'),
        ),
    ]
