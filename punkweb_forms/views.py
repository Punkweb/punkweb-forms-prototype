import json
from django.shortcuts import render, redirect
from punkweb_forms.dynamic_form import get_form_class
from punkweb_forms.models import Form, FormSubmission


def form_list_view(request):
    forms = Form.objects.all()
    return render(request, "punkweb_forms/form_list_view.html", {"forms": forms})


def form_view(request, form_id):
    form_instance = Form.objects.get(id=form_id)
    DynamicForm = get_form_class(form_id)

    if request.method == "POST":
        form = DynamicForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            data_json = json.dumps(data)
            FormSubmission.objects.create(form=form_instance, data=data_json)

            return redirect("punkweb_forms:form_list")
    else:
        form = DynamicForm()

    return render(
        request,
        "punkweb_forms/form_template.html",
        {"form": form, "form_instance": form_instance},
    )
