# Generated by Django 2.0 on 2021-04-15 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0023_auto_20210415_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, null=True)),
                ('year', models.CharField(max_length=300, null=True)),
                ('poster', models.URLField(default=None, null=True)),
                ('rating', models.FloatField(default=0)),
                ('director', models.CharField(max_length=300, null=True)),
                ('cast', models.CharField(max_length=800, null=True)),
                ('description', models.TextField(max_length=5000)),
                ('movie_id', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=5000)),
                ('rating', models.FloatField(default=0)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.MovieClass')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
