# Generated by Django 2.1.7 on 2019-04-01 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restAPI', '0003_auto_20190318_1608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='last_name',
        ),
    ]