# Generated by Django 4.0.2 on 2022-04-04 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='application_deadline',
            field=models.DateField(),
        ),
    ]
