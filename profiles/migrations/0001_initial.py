# Generated by Django 4.2.7 on 2024-03-05 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("post", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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
                ("image", models.ImageField(null=True, upload_to="profile")),
                ("first_name", models.CharField(blank=True, max_length=200, null=True)),
                ("last_name", models.CharField(blank=True, max_length=200, null=True)),
                ("bio", models.CharField(blank=True, max_length=200, null=True)),
                ("location", models.CharField(blank=True, max_length=200, null=True)),
                ("url", models.URLField(blank=True, null=True)),
                ("favourite", models.ManyToManyField(blank=True, to="post.post")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
