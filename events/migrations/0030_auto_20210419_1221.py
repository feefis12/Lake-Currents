# Generated by Django 3.1.7 on 2021-04-19 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0029_auto_20210419_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='relatedArtist',
            field=models.CharField(blank=True, default='The Strokes', max_length=120, verbose_name='Similar Artists'),
        ),
    ]
