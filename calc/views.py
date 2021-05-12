from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
# Create your views here.


def run(request):
    return render(request, template_name='calc/main.html')
