from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse("<h1>Olá MMPG Novais!!!</h1>")
    return render(request, "todos/home.html")