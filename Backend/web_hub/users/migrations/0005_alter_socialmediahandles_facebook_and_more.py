# Generated by Django 4.2.7 on 2024-02-27 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_userprofile_social_media_handles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediahandles',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='socialmediahandles',
            name='instagram',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='socialmediahandles',
            name='linkedin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='socialmediahandles',
            name='tiktok',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='socialmediahandles',
            name='x',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='social_media_handles',
            field=models.ManyToManyField(to='users.socialmediahandles'),
        ),
    ]
