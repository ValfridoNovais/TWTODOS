from django.contrib import admin
from django.urls import path

#from todos.views import todo_list
from todos.views import TodoListView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodoListView.as_view()),
    path("create", TodoCreatView.as_view())
    #path("", todo_list),
]
