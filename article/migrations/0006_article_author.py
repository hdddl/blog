# Generated by Django 3.2.5 on 2022-01-30 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_article_abstract'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default='Dongliu', max_length=50),
        ),
    ]