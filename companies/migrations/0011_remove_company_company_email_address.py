# Generated by Django 4.0.2 on 2022-03-25 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0010_alter_company_company_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='company_email_address',
        ),
    ]
