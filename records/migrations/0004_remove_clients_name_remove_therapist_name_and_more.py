# Generated by Django 4.2.2 on 2023-06-29 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_rename_client_id_records_client_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='name',
        ),
        migrations.RemoveField(
            model_name='therapist',
            name='name',
        ),
        migrations.AddField(
            model_name='clients',
            name='first_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='last_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='therapist',
            name='first_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='therapist',
            name='last_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
