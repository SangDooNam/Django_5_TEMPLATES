from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views import View

# Create your views here.

class MainView(View):
    
    def get(self, request):
        return render(request, "main/main.html")

