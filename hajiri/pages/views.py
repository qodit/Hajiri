from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect


def home(request):
    template = loader.get_template('pages/home.html')
    context = RequestContext(request, {
        'title': "Hajiri Dashboard",
        'mainmenuindex': 1,
    })

    return HttpResponse(template.render(context))
