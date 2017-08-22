from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie

from learn.models import Lesson, ExecutionStatus

import io
import json
import sys
import os
import base64
import traceback


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
    codeOut = io.StringIO()
    __original = os.getcwd()
    os.chdir("learn/static/images")
    sys.stdout = codeOut
    sys.stderr = codeOut
    try:
        exec(code)
    except:
        traceback.print_exc(file=sys.stdout)
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    output = codeOut.getvalue()
    codeOut.close()
    images = ""
    for file in os.listdir('.'):
        if file.endswith('_imshow.png'):
            with open(file, "rb") as image:
                images += "<figure><figcaption>" + file.rstrip(
                    "_imshow.png") + "</figcaption><img src=\"data:image/png;base64," + base64.b64encode(
                    image.read()) + "\"></figure><br>"
            os.unlink(file)
    os.chdir(__original)
    stat = ExecutionStatus.objects.create(user=request.user, lesson=lesson, program=None, code=code, output=output)
    return HttpResponse(json.dumps({'output': output, 'images': images}))
