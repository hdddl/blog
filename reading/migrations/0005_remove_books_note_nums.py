# Generated by Django 3.2.5 on 2022-10-15 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reading', '0004_auto_20221015_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='note_nums',
        ),
    ]
