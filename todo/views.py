from django.shortcuts import render, redirect, get_object_or_404

from .models import Todo
from .forms import TodoForm


def list_todo(request):
    todos = Todo.objects.all()
    context = {"todos": todos}
    return render(request, 'todo/list.html', context)


def create_todo(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('todo:list_todo')

    context = {"form": form}
    return render(request, 'todo/create_todo.html', context)


def delete_todo(request, todo_id):
    todo = Todo.objects.filter(id=todo_id)
    todo.delete()
    return redirect('todo:list_todo')


def update_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('todo:list_todo')

    context = {'form': form}
    return render(request, 'todo/update_todo.html', context)