# Generated by Django 4.2.7 on 2024-02-27 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_socialmediahandles_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='social_media_handles',
            field=models.ManyToManyField(blank=True, to='users.socialmediahandles'),
        ),
    ]
