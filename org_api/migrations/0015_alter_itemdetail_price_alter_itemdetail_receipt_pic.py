# Generated by Django 4.1.1 on 2022-09-20 04:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org_api', '0014_event_completed_alter_itemdetail_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdetail',
            name='price',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(7500.0)]),
        ),
        migrations.AlterField(
            model_name='itemdetail',
            name='receipt_pic',
            field=models.ImageField(blank=True, default='receipt_images/None--f8422ba8-06dd-4ad1-abea-f3f340ec3262.png', null=True, upload_to='receipt_images'),
        ),
    ]
