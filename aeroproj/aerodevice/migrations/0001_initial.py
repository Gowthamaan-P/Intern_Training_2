# Generated by Django 4.2.7 on 2023-11-28 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='devicedata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('serial_number', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('location', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='patentdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorid', models.CharField(max_length=255)),
                ('patentid', models.CharField(max_length=255)),
                ('patent_name', models.CharField(max_length=255)),
                ('patent_age', models.IntegerField()),
                ('patent_gender', models.CharField(max_length=255)),
                ('contact', models.IntegerField()),
                ('emergency', models.BooleanField(default=False)),
            ],
        ),
    ]