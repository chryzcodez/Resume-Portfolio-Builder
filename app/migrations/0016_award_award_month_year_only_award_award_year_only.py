# Generated by Django 4.1.1 on 2022-11-19 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0015_alter_experience_experience_start_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="award",
            name="award_month_year_only",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="award",
            name="award_year_only",
            field=models.BooleanField(default=False),
        ),
    ]