# Generated by Django 4.1.1 on 2022-09-22 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org_api', '0019_remove_family_approved_organizer_approved_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemdetail',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]