# Generated by Django 4.1.7 on 2023-02-22 08:32

import birthday.fields
import datetime
from django.db import migrations, models
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=1000, verbose_name='Comment')),
                ('date', models.DateTimeField(default=datetime.datetime(2023, 2, 22, 8, 32, 16, 976778, tzinfo=datetime.timezone.utc), verbose_name='Comment Date')),
            ],
        ),
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=50, verbose_name='Frist Name')),
                ('sName', models.CharField(max_length=50, verbose_name='Second Name')),
                ('education', models.CharField(max_length=80, verbose_name='Education')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('birthDay_dayofyear_internal', models.PositiveSmallIntegerField(default=None, editable=False, null=True)),
                ('birthDay', birthday.fields.BirthdayField()),
                ('phoneNumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region='EG')),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('content', models.TextField(max_length=1000, verbose_name='Content')),
                ('date', models.DateTimeField(default=datetime.datetime(2023, 2, 22, 8, 32, 16, 976778, tzinfo=datetime.timezone.utc), verbose_name='Post Date')),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('github_Url', models.URLField(verbose_name='Github Url')),
                ('about', models.TextField(max_length=1000, verbose_name='about')),
                ('fetures', models.TextField(max_length=1000, verbose_name='fetures')),
                ('techUses', models.CharField(max_length=500, verbose_name='Technologies Used')),
                ('date', models.DateTimeField(default=datetime.datetime(2023, 2, 22, 8, 32, 16, 976778, tzinfo=datetime.timezone.utc), verbose_name='Project Date')),
            ],
        ),
    ]