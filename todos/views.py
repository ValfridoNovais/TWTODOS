from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Todo, Product, Client  # Importe seus modelos
from .forms import TodoForm  # Importe o formulário

class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("todo_list")

class ProductListView(ListView):
    model = Product
    template_name = "todos/produtos.html"

class ClientListView(ListView):
    model = Client
    template_name = "todos/clientes.html"
