# Generated by Django 4.1.1 on 2023-10-18 07:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email address"
                    ),
                ),
                ("first_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=150)),
                ("is_active", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Levels",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Personal_Details",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("feedback_id", models.UUIDField(default=uuid.uuid4, editable=False)),
                (
                    "resume_name",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                ("full_name", models.CharField(max_length=300)),
                ("job_title", models.CharField(blank=True, max_length=100, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("phone", models.CharField(blank=True, max_length=13, null=True)),
                ("address", models.CharField(blank=True, max_length=400, null=True)),
                ("date_of_birth", models.DateField(blank=True, null=True)),
                (
                    "nationality",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "passport_id",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "marital_status",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "military_service",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "driving_license",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "gender_pronoun",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("website", models.CharField(blank=True, max_length=700, null=True)),
                ("twitter", models.CharField(blank=True, max_length=250, null=True)),
                ("github", models.CharField(blank=True, max_length=250, null=True)),
                ("linkedin", models.CharField(blank=True, max_length=250, null=True)),
                ("orcid", models.CharField(blank=True, max_length=250, null=True)),
                ("skype", models.CharField(blank=True, max_length=250, null=True)),
                ("discord", models.CharField(blank=True, max_length=250, null=True)),
                ("dribble", models.CharField(blank=True, max_length=250, null=True)),
                ("behance", models.CharField(blank=True, max_length=250, null=True)),
                ("medium", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "stackoverflow",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                ("gitlab", models.CharField(blank=True, max_length=250, null=True)),
                ("quora", models.CharField(blank=True, max_length=250, null=True)),
                ("facebook", models.CharField(blank=True, max_length=250, null=True)),
                ("instagram", models.CharField(blank=True, max_length=250, null=True)),
                ("hackerrank", models.CharField(blank=True, max_length=250, null=True)),
                ("wechat", models.CharField(blank=True, max_length=250, null=True)),
                ("kaggle", models.CharField(blank=True, max_length=250, null=True)),
                ("youtube", models.CharField(blank=True, max_length=250, null=True)),
                ("tiktok", models.CharField(blank=True, max_length=250, null=True)),
                ("signal", models.CharField(blank=True, max_length=250, null=True)),
                ("telegram", models.CharField(blank=True, max_length=250, null=True)),
                ("whatsapp", models.CharField(blank=True, max_length=250, null=True)),
                ("paypal", models.CharField(blank=True, max_length=250, null=True)),
                ("dev_to", models.CharField(blank=True, max_length=250, null=True)),
                ("angellist", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "producthunt",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                ("artstation", models.CharField(blank=True, max_length=250, null=True)),
                ("codepen", models.CharField(blank=True, max_length=250, null=True)),
                ("fiverr", models.CharField(blank=True, max_length=250, null=True)),
                ("hashnode", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "pluralsight",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "researchgate",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                ("imdb", models.CharField(blank=True, max_length=250, null=True)),
                ("qwiklabs", models.CharField(blank=True, max_length=250, null=True)),
                ("googleplay", models.CharField(blank=True, max_length=250, null=True)),
                ("tumbir", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "tripadvisor",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                ("yelp", models.CharField(blank=True, max_length=250, null=True)),
                ("qq", models.CharField(blank=True, max_length=250, null=True)),
                ("slack", models.CharField(blank=True, max_length=250, null=True)),
                ("flickr", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "reverbnation",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                ("deviantart", models.CharField(blank=True, max_length=250, null=True)),
                ("vimeo", models.CharField(blank=True, max_length=250, null=True)),
                ("reddit", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "pininterest",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                ("blogger", models.CharField(blank=True, max_length=250, null=True)),
                ("spotify", models.CharField(blank=True, max_length=250, null=True)),
                ("bitcoin", models.CharField(blank=True, max_length=250, null=True)),
                ("appstore", models.CharField(blank=True, max_length=250, null=True)),
                ("wordpress", models.CharField(blank=True, max_length=250, null=True)),
                ("leetcode", models.CharField(blank=True, max_length=250, null=True)),
                ("codechef", models.CharField(blank=True, max_length=250, null=True)),
                ("codeforces", models.CharField(blank=True, max_length=250, null=True)),
                ("vsco", models.CharField(blank=True, max_length=250, null=True)),
                ("snapchat", models.CharField(blank=True, max_length=250, null=True)),
                ("upwork", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "geeksforgeeks",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "googlescholar",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                ("line", models.CharField(blank=True, max_length=250, null=True)),
                ("tryhackme", models.CharField(blank=True, max_length=250, null=True)),
                ("coursera", models.CharField(blank=True, max_length=250, null=True)),
                ("protonmail", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "hackerearth",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                ("codewars", models.CharField(blank=True, max_length=250, null=True)),
                ("hackthebox", models.CharField(blank=True, max_length=250, null=True)),
                ("bitbucket", models.CharField(blank=True, max_length=250, null=True)),
                ("gitea", models.CharField(blank=True, max_length=250, null=True)),
                ("xing", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Skills",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("skill_name", models.CharField(max_length=80)),
                (
                    "skill_information",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "personal_detail",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.personal_details",
                    ),
                ),
                (
                    "skill_level",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app.levels",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Reference",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("reference_name", models.CharField(max_length=200)),
                (
                    "reference_job_title",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "reference_organisation",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "reference_phone",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                (
                    "reference_email",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                (
                    "reference_link",
                    models.CharField(blank=True, max_length=300, null=True),
                ),
                (
                    "personal_detail",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.personal_details",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Publication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("publisher", models.CharField(max_length=200)),
                ("publication_title", models.CharField(max_length=200)),
                ("publication_date", models.DateField(blank=True, null=True)),
                ("publication_description", models.TextField(blank=True, null=True)),
                (
                    "publication_link",
                    models.CharField(blank=True, max_length=300, null=True),
                ),
                ("publication_month_year_only", models.BooleanField(default=False)),
                ("publication_year_only", models.BooleanField(default=False)),
                (
                    "personal_detail",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.personal_details",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("project_title", models.CharField(max_length=200)),
                ("subtitle", models.CharField(blank=True, max_length=100, null=True)),
                ("project_start_date", models.DateField(blank=True, null=True)),
                ("project_end_date", models.DateField(blank=True, null=True)),
                ("project_description", models.TextField(blank=True, null=True)),
                ("project_current", models.BooleanField(default=False)),
                (
                    "project_link",
                    models.CharField(blank=True, max_length=300, null=True),
                ),
                ("project_month_year_only", models.BooleanField(default=False)),
                ("project_year_only", models.BooleanField(default=False)),
                (
                    "personal_detail",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.personal_details",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("summary", models.TextField()),
                (
                    "personal_detail",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.personal_details",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Organisation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("position", models.CharField(max_length=100)),
                ("organisation", models.CharField(max_length=100)),
                (
                    "organisation_city",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "organisation_country",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("organisation_start_date", models.DateField(blank=True, null=True)),
                ("organisation_end_date", models.DateField(blank=True, null=True)),
                ("organisation_description", models.TextField(blank=True, null=True)),
                ("organisation_current", models.BooleanField(default=False)),
                ("organisation_month_year_only", models.BooleanField(default=False)),
                ("organisation_year_only", models.BooleanField(default=False)),
                (
                    "organisation_link",
                    models.CharField(blank=True, max_length=300, null=True),
                ),
                (
                    "personal_detail",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.personal_details",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Language",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("language", models.CharField(max_length=200)),
                (
                    "language_additional_information",
                    models.CharField(blank=True, max_length=400, null=True),
                ),
                (
                    "language_level",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app.levels",
                    ),
                ),
                (
                    "personal_detail",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.personal_details",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Interest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("interest", models.CharField(max_length=150)),
                (
                    "interest_additional_information",
                    models.TextField(blank=True, null=True),
                ),
                (
                    "interest_link",
                    models.CharField(blank=True, max_length=300, null=True),
                ),
                (
                    "personal_detail",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.personal_details",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150)),
                ("comment", models.TextField()),
                ("time_created", models.DateTimeField(auto_now_add=True)),
                (
                    "personal_detail",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.personal_details",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Experience",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("experience_job_title", models.CharField(max_length=200)),
                ("employer", models.CharField(max_length=100)),
                (
                    "experience_city",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "experience_country",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "experience_start_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Experience Start Date"
                    ),
                ),
                ("experience_end_date", models.DateField(blank=True, null=True)),
                ("experience_description", models.TextField(blank=True, null=True)),
                ("experience_current", models.BooleanField(default=False)),
                (
                    "experience_link",
                    models.CharField(blank=True, max_length=300, null=True),
                ),
                ("experience_month_year_only", models.BooleanField(default=False)),
                ("experience_year_only", models.BooleanField(default=False)),
                (
                    "personal_detail",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.personal_details",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Education",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("school", models.CharField(max_length=70)),
                ("degree", models.CharField(max_length=100)),
                (
                    "education_city",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "education_country",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("education_start_date", models.DateField(blank=True, null=True)),
                ("education_end_date", models.DateField(blank=True, null=True)),
                ("education_description", models.TextField(blank=True, null=True)),
                ("education_current", models.BooleanField(default=False)),
                (
                    "education_link",
                    models.CharField(blank=True, max_length=300, null=True),
                ),
                ("education_month_year_only", models.BooleanField(default=False)),
                ("education_year_only", models.BooleanField(default=False)),
                (
                    "personal_detail",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.personal_details",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Certificate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("certificate", models.CharField(max_length=150)),
                (
                    "certificate_additional_information",
                    models.TextField(blank=True, null=True),
                ),
                (
                    "certificate_link",
                    models.CharField(blank=True, max_length=300, null=True),
                ),
                (
                    "personal_detail",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.personal_details",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Award",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("award", models.CharField(max_length=150)),
                ("issuer", models.CharField(blank=True, max_length=150, null=True)),
                ("award_description", models.TextField(blank=True, null=True)),
                ("award_date", models.DateField(blank=True, null=True)),
                ("award_link", models.CharField(blank=True, max_length=300, null=True)),
                ("award_month_year_only", models.BooleanField(default=False)),
                ("award_year_only", models.BooleanField(default=False)),
                (
                    "personal_detail",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.personal_details",
                    ),
                ),
            ],
        ),
    ]
