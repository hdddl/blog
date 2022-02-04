# Generated by Django 3.2.5 on 2022-02-02 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0023_remove_micro_blog_html_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='micro_blog',
            name='html_generate_date',
            field=models.DateTimeField(blank=True, null=True),
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
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='html_generate_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
