# Generated by Django 4.2.2 on 2023-11-26 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0014_clients_password_therapist_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='password',
        ),
        migrations.RemoveField(
            model_name='therapist',
            name='password',
        ),
        migrations.RemoveField(
            model_name='therapist',
            name='price',
        ),
    ]
