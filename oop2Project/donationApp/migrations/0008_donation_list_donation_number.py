# Generated by Django 5.0.6 on 2024-05-16 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donationApp', '0007_alter_donation_list_raised_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation_list',
            name='donation_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
