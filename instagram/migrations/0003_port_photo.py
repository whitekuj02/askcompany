# Generated by Django 3.0.14 on 2022-12-19 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_port_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='port',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]