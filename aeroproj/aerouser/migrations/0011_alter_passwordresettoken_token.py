# Generated by Django 4.2.7 on 2023-11-27 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aerouser', '0010_passwordresettoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresettoken',
            name='token',
            field=models.UUIDField(editable=False),
        ),
    ]
