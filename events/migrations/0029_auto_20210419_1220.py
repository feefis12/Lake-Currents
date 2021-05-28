# Generated by Django 3.1.7 on 2021-04-19 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0028_auto_20210419_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='favSongTitle3',
            field=models.CharField(blank=True, default=', ', max_length=120, verbose_name='Favorite Song'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='favSongUrl3',
            field=models.URLField(blank=True, default=', ', max_length=120, verbose_name='Song URL 3'),
        ),
    ]
