from django.shortcuts import redirect, render
from .forms import ItemsForms
from .models import TodoListModel
# Create your views here.
def Todo_list(request):
    itemsforms = ItemsForms()
    if request.method == "POST":
        itemsforms = ItemsForms(request.POST)
        todo_list = TodoListModel.objects.all()
        context = {
        "itemsforms":itemsforms,
        "todo_list":todo_list
        }
        if itemsforms.is_valid():
            itemsforms.save()
        return redirect('items')
    elif request.method == "GET":
        todo_list = TodoListModel.objects.all()
        context = {
        "itemsforms":itemsforms,
        "todo_list":todo_list
    }
    return render(request, 'pages/items.html', context)

def delete_all_todo(reqeust):
    TodoListModel.objects.all().delete()
    return redirect('items')

def complete_view(request,id):
    todo_complete = TodoListModel.objects.get(id=id)
    todo_complete.delete()
    return redirect('items')