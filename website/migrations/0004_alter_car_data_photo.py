# Generated by Django 4.0.3 on 2022-08-15 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_car_data_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_data',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='images/%Y/%m/%d'),
        ),
    ]