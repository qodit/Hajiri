from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from pages.models import TeacherRecord

def home(request):
    template = loader.get_template('home.html')

    records = TeacherRecord.objects.all()

    context = RequestContext(request, {
        'title': "Hajiri Dashboard",
        'mainmenuindex': 1,
        'records': records,
    })

    return HttpResponse(template.render(context))
