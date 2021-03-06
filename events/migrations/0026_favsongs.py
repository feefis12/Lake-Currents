# Generated by Django 3.1.7 on 2021-04-19 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0025_auto_20210417_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavSongs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, verbose_name='Song name')),
                ('url', models.CharField(blank=True, max_length=120, verbose_name='Timestamp')),
                ('songtag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.blogpost')),
            ],
        ),
    ]
