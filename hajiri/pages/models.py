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


class Record(models.Model):
    date = models.DateField()
    teacher = models.ForeignKey(Teacher)
    absent = models.IntegerField(default=0)
    present = models.IntegerField(default=0)

    def __str__(self):
        return "Record for "+self.teacher.name+" on "+str(self.date)


class TeacherRecord(models.Model):
    teacher = models.ForeignKey(Teacher)

    yp = models.IntegerField(default=0)  # Yesterday presents
    ya = models.IntegerField(default=0)  # Yesterday Absents

    twp = models.IntegerField(default=0)  # This week presents
    twa = models.IntegerField(default=0)  # This week Absents

    tmp = models.IntegerField(default=0)  # This month presents
    tma = models.IntegerField(default=0)  # This month Absents

    def __str__(self):
        return "Records for "+self.teacher.name

    def getPresent(self):
        return self.yp/(self.yp + self.ya)*100

    def getAbsent(self):
        return self.ya/(self.yp + self.ya)*100


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.name
