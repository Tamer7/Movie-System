# Generated by Django 2.0 on 2021-04-14 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_movietest_prod_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movietest',
            name='prod_img',
        ),
    ]
