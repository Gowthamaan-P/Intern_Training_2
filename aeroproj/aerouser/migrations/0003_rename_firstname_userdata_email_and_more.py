# Generated by Django 4.2.7 on 2023-11-22 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aerouser', '0002_userdata_joindate_userdata_phonenumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='firstname',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='userdata',
            old_name='lastname',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='joindate',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='phonenumber',
        ),
    ]
