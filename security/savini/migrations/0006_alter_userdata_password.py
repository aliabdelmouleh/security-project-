# Generated by Django 4.2.9 on 2024-04-25 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savini', '0005_rename_encrypted_password_userdata_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
