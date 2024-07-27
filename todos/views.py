from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .models import Todo

#def todo_list(request):
#    todos = Todo.objects.all()
#    return render(request, "todos/todo_list.html", {"todos": #todos})

class TodoListView(ListView):
    model = Todo

class TodoCreatView(CreateView):
    model = Todo