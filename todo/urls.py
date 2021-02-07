from django.urls import path

from .views import list_todo, create_todo, delete_todo, update_todo

app_name = 'todo'

urlpatterns = [
    path('', list_todo, name='list_todo'),
    path('create/', create_todo, name='create_todo'),
    path('<int:todo_id>/delete/', delete_todo, name='delete_todo'),
    path('<int:todo_id>/update/', update_todo, name='update_todo')
]

