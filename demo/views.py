from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    query_string = request.GET
    if len(query_string) == 0:
        return render(request, 'index.html')
    try:
        a = int(query_string.get('a'))
        b = int(query_string.get('b'))
    except:
        context = {'msg': 'error'}
        return render(request, 'index.html', context)
    context = {'ans': a+b}
    return render(request, 'index.html', context)