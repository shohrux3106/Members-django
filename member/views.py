from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Member
from django.template import loader
from django.urls import reverse

# Create your views here.
def hello(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('myfirst.html')
    context = {
        'mymembers':mymembers,
    }
    
    return HttpResponse(template.render(context, request))
    # return HttpResponse(output)

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    X = request.POST["first"]
    Y = request.POST["last"]
    member = Member(firstname=X, lastname=Y)
    member.save()
    return HttpResponseRedirect(reverse('hello'))

def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('hello'))

def update(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = Member.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('hello'))