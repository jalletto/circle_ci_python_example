# Generated by Django 4.0.2 on 2022-02-23 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_organizer', '0002_format_abbreviation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='format',
        ),
        migrations.AddField(
            model_name='movie',
            name='format',
            field=models.ManyToManyField(to='media_organizer.Format'),
        ),
    ]
