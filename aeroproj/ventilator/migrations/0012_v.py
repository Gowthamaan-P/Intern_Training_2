# Generated by Django 4.2.7 on 2023-12-02 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventilator', '0011_rename_userdevices_mydevices'),
    ]

    operations = [
        migrations.CreateModel(
            name='V',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
