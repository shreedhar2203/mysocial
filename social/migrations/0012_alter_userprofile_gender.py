# Generated by Django 4.2.2 on 2023-08-03 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0011_alter_userprofile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female')], default=1),
        ),
    ]
