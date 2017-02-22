from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext,loader

# Create your views here.
def index(request):
    template = loader.get_template('./query_app/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def detail(request,id):
    response = 'you are looking for a detail for %s'
    return HttpResponse(response % id)
