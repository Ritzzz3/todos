from django.shortcuts import render, redirect,get_object_or_404
from .models import*
# Create your views here.
def add_task(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        Task.objects.create(
            tasks = task
        )
        return redirect('home')
        
    tasks = Task.objects.all()
      
    return render(request , 'home.html', context={'tasks': tasks})

def update_task(request, task_id ):
    task = get_object_or_404(Task , id = task_id )
    
    if request.method =='POST':
        if 'important' in request.POST :
            task.important = not task.important
            task.save()
        else :
            task.complete = not task.complete
            task.save()
            
    return redirect('home')

def delete(request , task_id):
    Task.objects.get(id = task_id).delete()
    return redirect('home')
    