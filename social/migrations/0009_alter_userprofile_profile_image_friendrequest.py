# Generated by Django 4.2.2 on 2023-07-20 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0008_userpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_friend_requests', to='social.userprofile')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_friend_requests', to='social.userprofile')),
            ],
        ),
    ]
