# Generated by Django 5.0.6 on 2024-05-15 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donationApp', '0002_remove_user_details_bio_user_details_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='gender',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
