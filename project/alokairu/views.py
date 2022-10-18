from asyncio.windows_events import NULL
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

#index
def index(request):
    template = loader.get_template('index.html')
    kotxeak = Kotxe.objects.all()
    kotxealokatuatrue =[]
    kotxealokatuafalse =[]

    for x in kotxeak:
        if(x.alokatua):
            kotxealokatuatrue.append(x)
        else:
            kotxealokatuafalse.append(x)
    context = {
    'kotxealokatuatrue': kotxealokatuatrue,
    'kotxealokatuafalse': kotxealokatuafalse,
    }
    return HttpResponse(template.render(context, request))

#Management lists
def kotxeak(request):
    kotxeak = Kotxe.objects.all()
    template = loader.get_template('kotxeak.html')
    context = {
    'kotxeak': kotxeak,
    }
    return HttpResponse(template.render(context, request))

def pertsonak(request):
    pertsonak = Pertsona.objects.all()
    template = loader.get_template('pertsonak.html')
    context = {
    'pertsonak': pertsonak,
    }
    return HttpResponse(template.render(context, request))

#Delete
def delpertsona(request,id):
    Pertsona.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('pertsonak'))

def delkotxea(request,id):
    Kotxe.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('kotxeak'))

#Add
def addpertsona(request):
    template = loader.get_template('addpertsona.html')
    return HttpResponse(template.render())

def addkotxeatodb(request):
    kotxe = Kotxe()
    kotxe.save()
    return HttpResponseRedirect(reverse('kotxeak'))

@csrf_exempt
def addpertsonatodb(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    if firstname != "" and lastname != "": 
        pertsona = Pertsona(firstname = firstname, lastname = lastname)
        pertsona.save()
    return HttpResponseRedirect(reverse('pertsonak'))

#Update
def updatepertsona(request,id):
    pertsona = Pertsona.objects.get(id=id)
    template = loader.get_template('updatepertsona.html')
    context = {
    'pertsona': pertsona,
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def updatepertsonaondb(request,id):
    pertsona = Pertsona.objects.get(id=id)
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    if firstname != "" and lastname != "":
        newpertsona = Pertsona(id = pertsona.id ,firstname = firstname, lastname = lastname)
        newpertsona.save()
    return HttpResponseRedirect(reverse('pertsonak'))

def updatekotxea(request,id):
    kotxea = Kotxe.objects.get(id=id)
    pertsonak = Pertsona.objects.all()
    template = loader.get_template('updatekotxea.html')
    context = {
    'kotxea': kotxea,
    'pertsonak': pertsonak,
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def updatekotxeaondb(request,id):
    kotxea = Kotxe.objects.get(id=id)
    alokatua = request.POST['alokatua']
    hasieradata = request.POST['hasieradata']
    bukaeradata = request.POST['bukaeradata']
    pertsonaid = request.POST['pertsona']
    if pertsonaid != "":
        pertsonaobj = Pertsona.objects.get(id=pertsonaid)
        kotxea = Kotxe(id=kotxea.id ,alokatua = alokatua, hasieradata = hasieradata, bukaeradata= bukaeradata, pertsona = pertsonaobj)
    kotxea.save()
    return HttpResponseRedirect(reverse('kotxeak'))

#Alokatu
def alokatu(request,id):
    kotxea = Kotxe.objects.get(id=id)
    pertsonak = Pertsona.objects.all()
    template = loader.get_template('alokatu.html')
    context = {
    'kotxea': kotxea,
    'pertsonak': pertsonak,
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def alokatuondb(request,id):
    kotxea = Kotxe.objects.get(id=id)
    hasieradata = request.POST['hasieradata']
    bukaeradata = request.POST['bukaeradata']
    pertsonaid = request.POST['pertsona']
    if pertsonaid != "" and hasieradata != "" and bukaeradata != "":
        pertsonaobj = Pertsona.objects.get(id=pertsonaid)
        kotxea = Kotxe(id=kotxea.id ,alokatua = True, hasieradata = hasieradata, bukaeradata= bukaeradata, pertsona = pertsonaobj)
        kotxea.save()
    return HttpResponseRedirect(reverse('index'))