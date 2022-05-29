# Generated by Django 4.0.4 on 2022-05-22 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sailor', '0034_rename_address_complaints_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='duplicate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.CharField(blank=b'I01\n', default=None, max_length=100)),
                ('username', models.CharField(blank=b'I01\n', default=None, max_length=100)),
                ('room_no', models.CharField(blank=b'I01\n', default=None, max_length=20)),
                ('desc', models.TextField(blank=b'I01\n', default=None)),
                ('student_user', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]