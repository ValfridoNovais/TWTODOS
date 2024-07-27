from django.contrib import admin
from django.urls import path
from todos.views import TodoListView, TodoCreateView, ProductListView, ClientListView  # Importe suas visualizações

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodoListView.as_view(), name="todo_list"),
    path("create", TodoCreateView.as_view(), name="todo_create"),
    path("produtos/", ProductListView.as_view(), name="products"),
    path("clientes/", ClientListView.as_view(), name="clientes"),
]
