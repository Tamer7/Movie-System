# Generated by Django 2.0 on 2021-04-14 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_movietest_prod_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movietest',
            name='poster',
            field=models.URLField(default=None, null=True),
        ),
    ]
