# Generated by Django 4.2.6 on 2023-10-14 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_imei1_phones_imei_remove_phones_imei2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phones',
            name='brand',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='phones',
            name='model',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='phones',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]