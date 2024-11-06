from django.shortcuts import render
from django.http import HttpResponse

def institutions(request):
    return HttpResponse('institutions')


def institutions_types(request):
    return HttpResponse('institutions types')