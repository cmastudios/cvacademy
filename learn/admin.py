from django.contrib import admin
from learn.models import Lesson, ExecutionStatus

# Register your models here.
admin.site.register(Lesson)
admin.site.register(ExecutionStatus)

admin.site.site_header = "OpenCV Academy Admin"
admin.site.site_title = "OpenCV Academy"