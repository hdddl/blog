# Generated by Django 3.2.5 on 2022-02-02 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0030_auto_20220202_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='micro_blog',
            name='pubdate',
            field=models.DateField(),
        ),
    ]