# Generated by Django 2.0.5 on 2018-05-30 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20180530_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='href',
            field=models.TextField(default='', verbose_name='链接'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='link',
            name='text',
            field=models.TextField(verbose_name='链接内容'),
        ),
    ]
