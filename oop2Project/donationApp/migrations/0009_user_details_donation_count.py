# Generated by Django 5.0.6 on 2024-05-16 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donationApp', '0008_donation_list_donation_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='donation_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
