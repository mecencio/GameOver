# Generated by Django 3.2.6 on 2022-07-03 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_auto_20220703_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cancelrequest',
            name='order_date',
        ),
    ]
