# Generated by Django 4.2.11 on 2024-06-21 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Form",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="FormSubmission",
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
                ("data", models.TextField()),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
                (
                    "form",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="submissions",
                        to="punkweb_forms.form",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Field",
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
                ("label", models.CharField(max_length=255)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("text", "Text"),
                            ("textarea", "Textarea"),
                            ("number", "Number"),
                            ("date", "Date"),
                        ],
                        max_length=255,
                    ),
                ),
                ("required", models.BooleanField(default=True)),
                ("order", models.IntegerField()),
                (
                    "form",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fields",
                        to="punkweb_forms.form",
                    ),
                ),
            ],
        ),
    ]