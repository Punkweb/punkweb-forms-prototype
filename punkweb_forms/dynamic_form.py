from django import forms
from django.forms import widgets
from punkweb_forms.models import Field, Form


def get_form_class(form_id):
    instance = Form.objects.get(id=form_id)
    fields = Field.objects.filter(form=instance).order_by("order")

    field_dict = {}
    for field in fields:
        if field.type == "text":
            field_dict[field.label.lower()] = forms.CharField(
                label=field.label,
                required=field.required,
            )
        elif field.type == "textarea":
            field_dict[field.label.lower()] = forms.CharField(
                label=field.label,
                required=field.required,
                widget=widgets.Textarea,
            )
        elif field.type == "number":
            field_dict[field.label.lower()] = forms.IntegerField(
                label=field.label,
                required=field.required,
            )
        elif field.type == "date":
            field_dict[field.label.lower()] = forms.DateField(
                label=field.label,
                widget=widgets.SelectDateWidget,
                required=field.required,
            )

    DynamicForm = type("DynamicForm", (forms.Form,), field_dict)

    return DynamicForm
