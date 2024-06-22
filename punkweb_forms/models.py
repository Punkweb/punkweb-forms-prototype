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

    class Meta:
        ordering = (
            "form",
            "order",
        )

    def __str__(self):
        return f"{self.form} - {self.order} - {self.name} - {self.type}"


class FormSubmission(models.Model):
    form = models.ForeignKey(Form, related_name="submissions", on_delete=models.CASCADE)
    data = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-submitted_at",)

    def __str__(self):
        return f"{self.form} - {self.submitted_at}"
