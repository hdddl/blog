# Generated by Django 3.2.5 on 2022-02-08 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('img', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='content',
            new_name='image',
        ),
    ]
