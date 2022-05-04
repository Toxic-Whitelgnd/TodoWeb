from django.urls import path
from .views import *

urlpatterns = [
    # path('',home,name="home"),
    # path('create/',createtodo,name="create-todo"),
    # path('items/<int:pk>/',createitems,name="create-item")
    path('',TaskList.as_view(),name="tasks"),
    path('task/<int:pk>/',TaskDetail.as_view(),name="task"),
    path('task-create',TaskCreate.as_view(),name="task-create"),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name="task-update"),
    path('task-delete/<int:pk>/',TaskDelete.as_view(),name="task-delete"),

]
