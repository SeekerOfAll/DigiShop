# Generated by Django 3.1.5 on 2021-01-13 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeView', '0002_auto_20210113_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slideshow',
            name='action_url',
            field=models.URLField(default='http://http://127.0.0.1:8000', verbose_name='action url'),
        ),
    ]