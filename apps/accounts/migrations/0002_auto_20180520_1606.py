# Generated by Django 2.0.5 on 2018-05-20 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='airdrop',
            unique_together=set(),
        ),
    ]
