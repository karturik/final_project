# Generated by Django 4.0.4 on 2022-06-22 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moodle_test', '0003_question_subject_question_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='subject',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='topic',
            field=models.CharField(default='-', max_length=200),
        ),
    ]
