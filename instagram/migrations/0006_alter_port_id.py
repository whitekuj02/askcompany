# Generated by Django 4.1.4 on 2022-12-21 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("instagram", "0005_alter_port_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="port",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
