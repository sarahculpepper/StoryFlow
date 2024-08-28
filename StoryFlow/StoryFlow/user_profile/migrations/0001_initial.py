# Generated by Django 4.2.6 on 2024-03-07 00:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                (
                    "gender",
                    models.IntegerField(
                        choices=[(0, "None"), (1, "Female"), (2, "Male"), (3, "Other")],
                        default=0,
                    ),
                ),
                ("age", models.IntegerField(default=21)),
                (
                    "picture",
                    models.ImageField(blank=True, upload_to="profile_pictures/"),
                ),
            ],
        ),
    ]
