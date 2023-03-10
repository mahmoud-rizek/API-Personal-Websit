# Generated by Django 4.1.7 on 2023-02-22 08:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalSite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 22, 8, 36, 3, 695839, tzinfo=datetime.timezone.utc), verbose_name='Comment Date'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 22, 8, 36, 3, 695839, tzinfo=datetime.timezone.utc), verbose_name='Post Date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 22, 8, 36, 3, 695839, tzinfo=datetime.timezone.utc), verbose_name='Project Date'),
        ),
    ]
