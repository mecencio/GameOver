# Generated by Django 3.2.6 on 2022-07-05 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_auto_20220705_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancelrequest',
            name='employee',
            field=models.CharField(default='-', max_length=255, null=True, verbose_name='Respuesta:'),
        ),
    ]