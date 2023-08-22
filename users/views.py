from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from todo_list.models import TodoListModel
# Create your views here.


@login_required(login_url='login')
def home_view(request):
    todo_list = TodoListModel.objects.all()
    context = {
        "todo_list":todo_list
    }
    print(todo_list)
    return render(request, 'views/home.html',context)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            pass
    else:
        pass

    return render(request, 'views/login.html')

def register_view(request):
    register_form = CreateUserForm()
    if request.method == "POST":
        register_form = CreateUserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            user = register_form.cleaned_data.get('username')
            return redirect('login')
        
        else:
            pass
    return render(request,'views/register.html',{"register_form":register_form})