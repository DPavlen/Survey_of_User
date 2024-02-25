from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from . models import Survey, Question, Answer
# from surveys.utils import paginator_context

COUNT_POST = 10


def get_paginated_objects(objects, request):
    """Возвращает объекты с пагинацией."""
    paginator = Paginator(objects, COUNT_POST)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def survey_list(request):
    """Главная страница списка опросов пользователей."""
    # surveys = Survey.objects.all()
    surveys = Survey.objects.raw('SELECT * FROM surveys_survey')
    page_obj = get_paginated_objects(surveys, request)
    context = {
        'page_obj': page_obj,
    }
    return render(request, "surveys/index.html", context)