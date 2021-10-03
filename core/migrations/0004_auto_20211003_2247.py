# Generated by Django 3.0.5 on 2021-10-03 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211003_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='core/static/images/profile_pics/', verbose_name='Profile Photo'),
        ),
    ]