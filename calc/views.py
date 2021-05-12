from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
# Create your views here.


def start(request):
    return render(request, template_name='calc/main.html')

def calc(request):
    num1 = request.GET['num1']
    num2 = request.GET['num2']
    runtype = request.GET['type']
    if runtype=='divide' and num2 == '0':
        ctx = {
            'result':'division by zero'
        }
    elif runtype=='plus':
        ctx={
            'result':int(num1)+int(num2)
        }
    elif runtype=='minus':
        ctx={
            'result':int(num1)-int(num2)
        }
    elif runtype=='multiply':
        ctx={
            'result':int(num1)*int(num2)
        }
    elif runtype=='divide':
        ctx={
            'result':int(num1)/int(num2)
        }
    return render(request, 'calc/result.html', ctx)