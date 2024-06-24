# Generated by Django 4.2.11 on 2024-06-23 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("punkweb_forms", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="field",
            name="widget",
            field=models.CharField(
                blank=True,
                help_text="Optional custom widget class as a dotted path",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="field",
            name="widget_options",
            field=models.TextField(
                blank=True, default="{}", help_text="JSON string of widget options"
            ),
        ),
    ]
