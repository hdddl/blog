# Generated by Django 3.2.5 on 2022-02-02 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0014_auto_20220201_2217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='micro_blog',
            name='content',
        ),
        migrations.AddField(
            model_name='micro_blog',
            name='html_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='micro_blog',
            name='markdown_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='micro_blog',
            name='modify_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='micro_blog',
            name='pubdate',
            field=models.DateField(verbose_name='发布时间'),
        ),
    ]