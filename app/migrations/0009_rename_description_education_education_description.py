# Generated by Django 4.1.1 on 2022-10-31 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0008_rename_skilll_level_skills_skill_level"),
    ]

    operations = [
        migrations.RenameField(
            model_name="education",
            old_name="description",
            new_name="education_description",
        ),
    ]