# Generated by Django 4.0.4 on 2022-04-28 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sailor', '0003_alter_students_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='img',
            field=models.ImageField(upload_to='media/pics'),
        ),
    ]
