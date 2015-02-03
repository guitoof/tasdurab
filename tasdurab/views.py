from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def home(request):

    #if user.is_authenticated:

    template = loader.get_template('index.html')
    context = RequestContext(request, {
        #'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))
