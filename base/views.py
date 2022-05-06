from difflib import context_diff
from re import template
from django.http import HttpResponseRedirect
from .models import *
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin #this will restrict the user to view thec ontent without login

# Create your views here.

def home(request):
    username = None
    email = None
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email
        print(username)
        print(email)
    else:
        username = "Guest"
    context = {'name':username,'email':email}
    return render(request,'base/home.html',context)


class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks' 
    #this will look for a template name task_list.html,so just create that template and add it to the html page
    def  get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-task') or '' 
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__istartswith=search_input
            )
            context['search_input'] = search_input

        return context


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'tasks'
    #this will look for task_detail.html,so just create that template and add it to the html page
    #but we dcdan customize it by using the template_name
    template_name = 'base/task.html'

class TaskCreate(CreateView):
    model = Task
    fields = ['title','description','complete']
    #this will also look for a template name task_form.html,so just create that,the task is the mdel name all in lowercases
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)

class TaskUpdate(UpdateView):
    model = Task
    fields = ['title','description','complete']
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

























# def home(request):
#     username = None
#     email = None
#     if request.user.is_authenticated:
#         username = request.user.username
#         email = request.user.email
#         print(username)
#         print(email)
#     else:
#         username = "Guest"
#     context = {'form':Todolist.objects.all,'fromls':tasks.objects.all,'name':username,'email':email}
#     return render(request,'base/home.html',context)

# def createtodo(request):
#     print('came here')
#     form = Createlist(request.POST)
#     print(form)
#     if request.method == 'POST':

#         if form.is_valid():
#             print('came inside the form')
#             n = form.cleaned_data["name"]
#             print(n)
#             t = Todolist(name=n)
#             t.save()
#             request.user.todolist.add(t)
#         return HttpResponseRedirect("/%i" %t.id) 

#     else:
#         print('nothing')
    
#     return render(request,'base/createtodolist.html',{'form':form})

# def createitems(request,pk):
#     t = Todolist.objects.get(id=pk)
#     print(t)
#     form = Createitemlist(request.POST)
#     print(form)
#     if request.method == 'POST':
#         print('came to psot')
#         if form.is_valid():
#             print('came inside the form')
#             n = form.cleaned_data.get("text")
            
#             t = tasks(text=n,todolist=t)
#             t.save()
#             return redirect('/')
#         else:
#             print("what the fk happenend ")
    
#     i = tasks.objects.all()
#     context = {'ti':t,'i':i}
#     return render(request,'base/todoitems.html',context)

