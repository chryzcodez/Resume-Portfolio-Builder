# Generated by Django 3.2.4 on 2021-08-17 19:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_resume', '0002_alter_user_mobile_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='year_from',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experience',
            name='year_to',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
