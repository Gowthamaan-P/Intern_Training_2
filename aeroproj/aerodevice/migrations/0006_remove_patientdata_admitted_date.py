# Generated by Django 4.2.7 on 2023-12-18 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aerodevice', '0005_post_patientdata_admitted_date_patientdata_blood_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientdata',
            name='admitted_date',
        ),
    ]
