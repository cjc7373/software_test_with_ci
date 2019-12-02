from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    query_string = request.GET
    try:
        a = int(query_string.get('a'))
        b = int(query_string.get('b'))
    except TypeError:
        return HttpResponse("Please input a and b.")
    return HttpResponse(a+b)