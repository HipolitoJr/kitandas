from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Cliente

# Create your views here.
def index(request):
    template = loader.get_template("clientes/index.html")
    clientes_lista = Cliente.objects.all()
    context = {
        "clientes_lista": clientes_lista,
    }
    return HttpResponse(template.render(context, request))
