# Generated by Django 3.2.5 on 2022-02-01 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_alter_blog_html_generate_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='html_generate_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='html_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]