# Generated by Django 4.0.2 on 2022-04-04 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_user_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.TextField(default='moore', unique=True),
            preserve_default=False,
        ),
    ]
