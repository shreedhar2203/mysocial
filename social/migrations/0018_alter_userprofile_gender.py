# Generated by Django 4.2.2 on 2023-08-04 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0017_alter_userprofile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(default='unknown', max_length=10),
        ),
    ]
