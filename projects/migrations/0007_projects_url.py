# Generated by Django 5.0.6 on 2024-07-22 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_projects_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='url',
            field=models.TextField(default='default.png'),
        ),
    ]
