# Generated by Django 4.0.4 on 2022-05-11 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_site', '0015_alter_teacher_teacher_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_img',
            field=models.ImageField(blank=True, default='user.jpg', null=True, upload_to='teacher_pics'),
        ),
    ]