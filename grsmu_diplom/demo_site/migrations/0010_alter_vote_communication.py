# Generated by Django 4.0.4 on 2022-05-06 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_site', '0009_alter_vote_communication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='communication',
            field=models.IntegerField(default=0),
        ),
    ]
