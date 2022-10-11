# Generated by Django 4.1.2 on 2022-10-08 16:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
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
                ("name", models.CharField(max_length=50, verbose_name="Project name")),
                (
                    "time_created",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
    ]