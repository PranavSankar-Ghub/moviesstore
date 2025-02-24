# Generated by Django 3.2.20 on 2024-09-06 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='synopsis',
        ),
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='movie_posters/'),
        ),
    ]
