# Generated by Django 4.1.1 on 2022-09-19 03:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org_api', '0013_alter_itemdetail_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='itemdetail',
            name='price',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(7500.0)]),
        ),
        migrations.AlterField(
            model_name='itemdetail',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
    ]
