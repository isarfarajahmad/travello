from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html',{'name':'MS Ahmad'})

def calc(request):

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    res2 = val1 - val2

    return render(request, 'result.html', {'result': res}, {'result2': res2})
