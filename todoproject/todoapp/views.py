from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoUpdateForm
from . models import todo
# Create your views here by function.
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class TaskListView(ListView):
    model=todo
    template_name = 'index.html'
    context_object_name = 'taskdetails'

class TaskDetailView(DetailView):
    model=todo
    template_name = 'detail.html'
    context_object_name = 'taskdetails'
class TaskUpdateView(UpdateView):
    model=todo
    template_name = 'cbvupdate.html'
    context_object_name = 'task'
    fields=('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cdvDetailView',kwargs={'pk':self.object.id})
class TaskDeleteView(DeleteView):
    model=todo
    template_name = 'delete.html'
    success_url = reverse_lazy('cdvListView')
# Create your views here by function.
def index(request):
    taskdetails=todo.objects.all();
    if request.method=='POST':
        name=request.POST.get('name','')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task=todo(name=name,priority=priority,date=date)
        print(task)
        task.save()
        return redirect('/')
    return render(request,'index.html',{'taskdetails':taskdetails})

def home(request):

    return render(request,'home.html')
def delete(request,id):
      task=todo.objects.get(id=id)
      if request.method=="POST":
         task.delete()
         return redirect('/')
      return render(request,'delete.html')


def update(request, id):
    task = todo.objects.get(id=id)
    f = TodoUpdateForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'update.html', {'form': f, 'task': task})

