from django.contrib import admin
from punkweb_forms.models import Form, Field, FormSubmission


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = (
        "label",
        "type",
    )


@admin.register(FormSubmission)
class FormSubmissionAdmin(admin.ModelAdmin):
    list_display = (
        "form",
        "submitted_at",
    )
