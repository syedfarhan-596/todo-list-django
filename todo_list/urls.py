from django.contrib import admin
from django.urls import path
from .views import Todo_list, delete_all_todo, complete_view

urlpatterns = [
    path('', Todo_list, name="items"),
    path('delete/',delete_all_todo,name="delete"),
    path('complete/<int:id>', complete_view, name="complete" )

]
