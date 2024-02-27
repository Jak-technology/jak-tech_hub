# Generated by Django 4.2.7 on 2024-01-26 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_creation', '0007_alter_project_image_alter_projectcomment_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='/images/project_images/default.jpg', upload_to='images/project_images/uploads/%Y/%m-%d/'),
        ),
        migrations.AlterField(
            model_name='projectcomment',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='project_creation.project'),
        ),
    ]
