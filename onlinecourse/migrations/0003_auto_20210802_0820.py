# Generated by Django 3.1.3 on 2021-08-02 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20210801_1711'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='chocies',
            new_name='choices',
        ),
    ]
