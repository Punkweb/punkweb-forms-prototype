from django.db import models


class Form(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Field(models.Model):
    form = models.ForeignKey(Form, related_name="fields", on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    type = models.CharField(
        max_length=255,
        choices=[
            ("text", "Text"),
            ("textarea", "Textarea"),
            ("number", "Number"),
            ("date", "Date"),
        ],
    )
    required = models.BooleanField(default=True)
    order = models.IntegerField()


class FormSubmission(models.Model):
    form = models.ForeignKey(Form, related_name="submissions", on_delete=models.CASCADE)
    data = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
