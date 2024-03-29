# Generated by Django 4.1 on 2023-06-23 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('markdown_text', models.TextField(verbose_name='日记内容 MarkDown')),
                ('html_text', models.TextField(verbose_name='日记内容 HTML')),
                ('pubData', models.DateField(verbose_name='日记时间')),
            ],
        ),
    ]
