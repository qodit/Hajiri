from django.db import models
from hajiri import settings
from django.contrib.auth.models import User


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Period(models.Model):
    teacher = models.ForeignKey(Teacher)
    subject = models.ForeignKey(Subject)
    dayid = models.IntegerField(default=1)
    periodid = models.IntegerField(default=1)

    def __str__(self):
        return self.subject.name+" by "+self.teacher.name+": period "+str(self.periodid)+" on  day "+str(self.dayid)

