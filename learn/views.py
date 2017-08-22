import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie

from learn.models import Lesson, ExecutionStatus
from . import code_execution


# Create your views here.

@login_required
def index(request):
    lessons = Lesson.objects.order_by('id')
    return HttpResponse(render(request, "learn/index.html", {"lessons": lessons}))


@login_required
@ensure_csrf_cookie
def lesson(request, lesson_id):
    les = get_object_or_404(Lesson, pk=lesson_id)
    return HttpResponse(render(request, "learn/lesson.html", {"lesson": les}))


@login_required
def compile(request):
    code = request.POST.get('code')
    lid = request.POST.get('lessonid')
    lesson = None
    if lid is not None:
        lesson = get_object_or_404(Lesson, pk=lid)

    result = code_execution.compile_execute(code, code_execution.ProgramLanguage(lesson.language))

    ExecutionStatus.objects.create(user=request.user, lesson=lesson, program=None, code=code, output=result.output)
    return HttpResponse(json.dumps({'output': result.output, 'images': result.images}))
