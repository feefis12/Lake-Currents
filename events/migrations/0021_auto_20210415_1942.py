# Generated by Django 3.1.7 on 2021-04-16 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0020_auto_20210415_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('Show', 'show'), ('Gallery', 'gallery'), ('Bar', 'bar'), ('Pop-up', 'pop-up'), ('Other', 'other')], default='show', max_length=120, verbose_name='Category'),
        ),
    ]