from django.urls import path
from . import views

app_name = "surveys"

urlpatterns = [
    path("surveys/", views.survey_list, name="survey_list"),
]