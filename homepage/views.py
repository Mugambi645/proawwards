from django.shortcuts import render,redirect
from .models import Projects,Review
from .forms import ProjectForm,RateForm
# Create your views here.
def index(request):
    """
    homepage url
    """
    projects = Projects.objects.all()
    return render(request,'home/index.html',{"projects":projects})
  
def new_project(request):
    """
    function to create a new profile from the Projects model
    Args:
    request: HttpRequest object containing data about this function
    """
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid:
            new_proj = form.save(commit = False)
            new_proj.save()
        return redirect('homepage:index')  
    else:
        form = ProjectForm()
    return render(request,'projects/new_project.html',{'form':form})    

def projects(request,id):
    project = Projects.objects.get(id = id)
    return render(request,'projects/read_more.html',{"projects":project})
 
