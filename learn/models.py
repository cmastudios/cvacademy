from django.db import models
from django.conf import settings

PROGRAM_LANGUAGE = (
    (1, "Python 3"),
    (2, "C++")
)


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    plan = models.TextField()
    code = models.TextField()
    language = models.IntegerField(choices=PROGRAM_LANGUAGE, default=1)

    def __str__(self):
        return self.title


class Program(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.TextField()
    language = models.IntegerField(choices=PROGRAM_LANGUAGE, default=1)

    def __str__(self):
        return self.name


class ExecutionStatus(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, null=True)
    program = models.ForeignKey(Program, null=True)
    time = models.DateTimeField(auto_now=True)
    code = models.TextField()
    output = models.TextField()

    def __str__(self):
        return "%s %s" % (self.user.get_username(), self.time)
