# Generated by Django 4.0.4 on 2022-05-09 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='slug',
            field=models.SlugField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='phone',
            name='release_date',
            field=models.CharField(max_length=255),
        ),
    ]
