from django import forms
from punkweb_forms.models import Field, Form


def get_field_class(type):
    field_classes = {
        "boolean": forms.BooleanField,
        "char": forms.CharField,
        "choice": forms.ChoiceField,
        "date": forms.DateField,
        "datetime": forms.DateTimeField,
        "decimal": forms.DecimalField,
        "duration": forms.DurationField,
        "email": forms.EmailField,
        "file": forms.FileField,
        "filepath": forms.FilePathField,
        "float": forms.FloatField,
        "image": forms.ImageField,
        "integer": forms.IntegerField,
        "multiplechoice": forms.MultipleChoiceField,
        "time": forms.TimeField,
        "url": forms.URLField,
        "uuid": forms.UUIDField,
    }
    return field_classes.get(type)


def get_form_class(form_id):
    instance = Form.objects.get(id=form_id)
    fields = Field.objects.filter(form=instance).order_by("order")

    field_dict = {}
    for field in fields:
        klass = get_field_class(field.type)
        field_dict[field.name] = klass(required=field.required)
        field_kwargs = {
            "required": field.required,
            "label": field.label or None,
            "help_text": field.help_text or None,
            "disabled": field.disabled,
        }
        field_kwargs = {k: v for k, v in field_kwargs.items() if v is not None}
        field_dict[field.name] = klass(**field_kwargs)

    DynamicForm = type("DynamicForm", (forms.Form,), field_dict)

    return DynamicForm
