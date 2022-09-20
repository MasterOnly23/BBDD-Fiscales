from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest


# Create your views here.

class Formularios_backup(HttpRequest):

    def home(request):
        return render(request, 'homeBackup.html')