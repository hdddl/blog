# Generated by Django 3.2.5 on 2022-02-02 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0019_micro_blog_html_generate_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='micro_blog',
            name='pubdate',
            field=models.DateTimeField(),
        ),
    ]
