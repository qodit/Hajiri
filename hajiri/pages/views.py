from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from pages.models import Record, Teacher
from django.shortcuts import render,redirect,get_object_or_404

def teachernames():
    teachernames = []
    teachers = Teacher.objects.all()
    for teacher in teachers:
        teachernames.append((teacher.pk, teacher.name))
    return teachernames

def home(request):
    import datetime

    yesterday = datetime.date.today() - datetime.timedelta(days=1)

    template = loader.get_template('home.html')

    records = Record.objects.filter(date = yesterday)

    teachers = []
    for record in records:
        teachers.append((record.teacher.name, record.present, record.absent))
    context = RequestContext(request, {
        'title': "Hajiri Dashboard",
        'mainmenuindex': 1,
        'teacherrecords': teachers,
        'teachers': teachernames(),
    })

    return HttpResponse(template.render(context))

def graph(request):
    records = Record.objects.all()
    teachers = Teacher.objects.all()

    teachername = []
    for teacher in teachers:
        teachername.append(teachers)

    data = []
    for record in records:
        onerecord = []

    template = loader.get_template('graph.html')
    context = RequestContext(request, {
        'title': "Hajiri Graph for Teachers",
        'mainmenuindex': 1,
        'teachers': teachernames(),
    })

    return HttpResponse(template.render(context))

def teacherinfo(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    template = loader.get_template('teacher.html')
    context = RequestContext(request, {
        'title': "Info about ",
        'mainmenuindex': 1,
        'teachers': teachernames(),
        'teacher': teacher,
    })

    return HttpResponse(template.render(context))
