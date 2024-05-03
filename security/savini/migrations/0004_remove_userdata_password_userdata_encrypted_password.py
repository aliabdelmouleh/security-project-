# Generated by Django 4.2.9 on 2024-04-25 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savini', '0003_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='password',
        ),
        migrations.AddField(
            model_name='userdata',
            name='encrypted_password',
            field=models.BinaryField(null=True),
        ),
    ]
