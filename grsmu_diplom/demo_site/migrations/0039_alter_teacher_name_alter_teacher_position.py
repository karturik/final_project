# Generated by Django 4.0.4 on 2022-05-22 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_site', '0038_remove_comment_dislikes_remove_comment_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='position',
            field=models.CharField(max_length=70),
        ),
    ]
