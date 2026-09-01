from django.shortcuts import render
from django import views

# Create your views here.

class IndexView(views.View):

    def get(self, request):
        return render(request, "main/index.html")