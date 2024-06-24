import json

from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class Form(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("punkweb_forms:form", args=[self.id])


class Field(models.Model):
    form = models.ForeignKey(Form, related_name="fields", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    required = models.BooleanField(default=True)
    label = models.CharField(max_length=255, blank=True)
    help_text = models.TextField(blank=True)
    disabled = models.BooleanField(default=False)
    type = models.CharField(
        max_length=255,
        choices=[
            ("boolean", "Boolean"),
            ("char", "Char"),
            ("choice", "Choice"),
            ("date", "Date"),
            ("datetime", "Datetime"),
            ("decimal", "Decimal"),
            ("duration", "Duration"),
            ("email", "Email"),
            ("file", "File"),
            ("filepath", "Filepath"),
            ("float", "Float"),
            ("image", "Image"),
            ("integer", "Integer"),
            ("multiplechoice", "MultipleChoice"),
            ("time", "Time"),
            ("url", "URL"),
            ("uuid", "UUID"),
        ],
    )
    order = models.IntegerField()
    widget = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Optional custom widget class as a dotted path",
    )
    widget_options = models.TextField(
        blank=True, default="{}", help_text="JSON string of widget options"
    )

    class Meta:
        ordering = (
            "form",
            "order",
        )

    def __str__(self):
        return f"{self.form} - {self.order} - {self.name} - {self.type}"

    def clean(self):
        super().clean()
        try:
            if self.widget_options:
                json.loads(self.widget_options)
        except json.JSONDecodeError:
            raise ValidationError("Invalid JSON for widget options")


class FormSubmission(models.Model):
    form = models.ForeignKey(Form, related_name="submissions", on_delete=models.CASCADE)
    data = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-submitted_at",)

    def __str__(self):
        return f"{self.form} - {self.submitted_at}"
