# Generated by Django 3.1.7 on 2021-04-16 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0018_event_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('show', 'DIY Show'), ('gallery', 'Gallery'), ('bar', 'Bar'), ('pop-up', 'Pop-up'), ('other', 'Other')], default='show', max_length=120, verbose_name='Category'),
        ),
    ]