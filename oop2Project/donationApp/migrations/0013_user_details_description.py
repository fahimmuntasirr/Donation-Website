# Generated by Django 5.0.6 on 2024-05-16 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donationApp', '0012_donation_details_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
