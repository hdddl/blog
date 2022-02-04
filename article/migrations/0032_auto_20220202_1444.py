# Generated by Django 3.2.5 on 2022-02-02 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0031_alter_micro_blog_pubdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pages',
            old_name='text',
            new_name='markdown_text',
        ),
        migrations.AddField(
            model_name='pages',
            name='html_generate_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pages',
            name='html_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pages',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pages',
            name='text_type',
            field=models.CharField(default='markdown', max_length=20),
        ),
    ]
