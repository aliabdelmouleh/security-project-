# Generated by Django 4.2.9 on 2024-04-25 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savini', '0007_userprofile_encryptedpassword'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='password',
        ),
        migrations.AddField(
            model_name='userdata',
            name='encrypted_password',
            field=models.BinaryField(default=b''),
        ),
        migrations.DeleteModel(
            name='EncryptedPassword',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
