# Generated by Django 4.2.7 on 2024-02-27 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='github_account',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
