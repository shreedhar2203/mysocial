# Generated by Django 4.2.2 on 2023-07-14 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(default='unknown', max_length=10),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='interest',
            field=models.CharField(default='unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.TextField(default='unknown'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phn_num',
            field=models.CharField(default='0000000000', max_length=10),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='school',
            field=models.CharField(default='unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
    ]
