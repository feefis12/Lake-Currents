# Generated by Django 3.1.7 on 2021-03-29 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20210328_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='fbLink',
            field=models.URLField(blank=True, verbose_name='FB Link'),
        ),
        migrations.AddField(
            model_name='event',
            name='flyer',
            field=models.ImageField(blank=True, upload_to='media/flyers'),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, max_length=120, verbose_name='Event Location'),
        ),
    ]
