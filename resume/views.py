from django.http import HttpResponse
from django.template import loader

def modelo(request):
    template = loader.get_template("resume/modelo.html")
    context = {}
    return HttpResponse(template.render(context, request))
