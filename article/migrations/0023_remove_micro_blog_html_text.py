# Generated by Django 3.2.5 on 2022-02-02 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0022_auto_20220202_0929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='micro_blog',
            name='html_text',
        ),
    ]
