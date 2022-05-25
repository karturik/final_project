# Generated by Django 4.0.4 on 2022-05-25 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.CharField(blank=True, choices=[('images/teacher.jpg', 'Billi'), ('images/van.jpg', 'Van')], default='images/teacher.jpg', max_length=255),
        ),
    ]
