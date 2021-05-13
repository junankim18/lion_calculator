from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'calc'

urlpatterns = [
    path('', view=views.start, name='home'),
    path('result', view=views.calc, name='result')
]
