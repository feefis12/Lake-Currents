# Generated by Django 3.1.7 on 2021-04-19 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0027_auto_20210419_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='favSongUrl',
            field=models.URLField(blank=True, max_length=120, verbose_name='Song URL 1'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='favSongUrl2',
            field=models.URLField(blank=True, max_length=120, verbose_name='Song URL 2'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='favSongUrl3',
            field=models.URLField(blank=True, max_length=120, verbose_name='Song URL 3'),
        ),
    ]
