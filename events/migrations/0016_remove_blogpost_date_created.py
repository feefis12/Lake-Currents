# Generated by Django 3.1.7 on 2021-04-05 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_email_musicform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='date_created',
        ),
    ]
