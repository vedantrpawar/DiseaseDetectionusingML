# Generated by Django 3.0.5 on 2021-10-03 17:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210917_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default=None, null=True, upload_to='core/static/images/profile_pics/', verbose_name='Profile Photo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='patients',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Patients Doctor is Treating'),
        ),
    ]