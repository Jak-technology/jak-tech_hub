# Generated by Django 4.2.7 on 2024-01-23 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogpost_date_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpostcomment',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blogpostcomment',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
