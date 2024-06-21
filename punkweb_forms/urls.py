from django.urls import path

from punkweb_forms import views

app_name = "punkweb_forms"
urlpatterns = [
    path("", views.form_list_view, name="form_list"),
    path("<int:form_id>/", views.form_view, name="form"),
]
