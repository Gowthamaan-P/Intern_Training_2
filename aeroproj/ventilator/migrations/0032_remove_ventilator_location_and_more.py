# Generated by Django 4.2.7 on 2023-12-18 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventilator', '0031_alter_device_logs_log_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ventilator',
            name='location',
        ),
        migrations.AddField(
            model_name='ventilator',
            name='battery_mfg_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ventilator',
            name='battery_no',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='ventilator',
            name='lot_no',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='ventilator',
            name='model_no',
            field=models.CharField(default=888, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ventilator',
            name='product',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='ventilator',
            name='product_id',
            field=models.CharField(default=1, max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
