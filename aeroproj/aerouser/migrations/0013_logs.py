# Generated by Django 4.2.7 on 2023-11-30 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aerouser', '0012_alter_passwordresettoken_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=50, unique=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('log_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]