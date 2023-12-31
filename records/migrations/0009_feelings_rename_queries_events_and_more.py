# Generated by Django 4.2.2 on 2023-07-03 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0008_alter_records_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feelings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Queries',
            new_name='Events',
        ),
        migrations.RenameField(
            model_name='therapist',
            old_name='queries_ids',
            new_name='events',
        ),
        migrations.RenameField(
            model_name='therapist',
            old_name='method_ids',
            new_name='methods',
        ),
        migrations.AddField(
            model_name='therapist',
            name='feelings',
            field=models.ManyToManyField(to='records.feelings'),
        ),
    ]
