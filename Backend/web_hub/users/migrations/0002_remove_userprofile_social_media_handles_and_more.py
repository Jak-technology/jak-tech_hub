# Generated by Django 4.2.7 on 2023-12-20 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='social_media_handles',
        ),
        migrations.DeleteModel(
            name='SocialMediaHandles',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='social_media_handles',
            field=models.CharField(default='X', max_length=100),
        ),
    ]
