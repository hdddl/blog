# Generated by Django 3.2.5 on 2022-02-04 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0034_auto_20220202_1502'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-pubdate'], 'verbose_name_plural': '博客'},
        ),
        migrations.AlterModelOptions(
            name='micro_blog',
            options={'ordering': ['-pubdate'], 'verbose_name_plural': '微博'},
        ),
    ]