from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from pages.models import Record

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
    })

    return HttpResponse(template.render(context))

def graph(request):
    records = Record.objects.all()

    template = loader.get_template('graph.html')
    context = RequestContext(request, {
        'title': "Hajiri Graph for Teachers",
        'mainmenuindex': 1,
    })

    return HttpResponse(template.render(context))
