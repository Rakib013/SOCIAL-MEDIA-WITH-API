# Generated by Django 3.2.8 on 2021-10-18 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0002_auto_20211018_0628'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cover_avatar',
            field=models.ImageField(default='images/avatar.svg', upload_to='cover/'),
        ),
    ]
