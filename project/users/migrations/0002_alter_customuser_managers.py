# Generated by Django 5.0.1 on 2024-01-19 06:19

import users.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', users.managers.UserManager()),
            ],
        ),
    ]
