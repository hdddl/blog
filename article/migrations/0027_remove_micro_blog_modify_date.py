# Generated by Django 3.2.5 on 2022-02-02 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0026_alter_micro_blog_modify_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='micro_blog',
            name='modify_date',
        ),
    ]