# Generated by Django 4.2.2 on 2023-07-17 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_userprofile_dob_userprofile_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(upload_to='profile_images/'),
        ),
    ]