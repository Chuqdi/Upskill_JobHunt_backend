# Generated by Django 4.0.2 on 2022-03-01 12:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0003_assignment_material_type_topic_material_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='topic',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
