# Generated by Django 2.0.3 on 2018-04-03 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20180403_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='img',
            field=models.ImageField(blank=True,
                                    default='avatar/blank_profile.png',
                                    upload_to='avatar'),
        ),
    ]
