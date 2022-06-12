from django.shortcuts import render, redirect
from .models import Project, Blog
from .forms import  ProjectForm, BlogForm
   


# Create your views here.


def homepage(request):
    projects=Project.objects.all()
    blogs = Blog.objects.all()
    context={'projects': projects, "blogs":blogs,}
    return render(request, "base/index.html",context)
    


"""def github(request,pk):
    github=Project.objects.get(id=pk)
    context = {'github': github}
    return render(request, "base/Github_Redirect.html",context)"""



def projectPage(request,pk):
    project = Project.objects.get(id=pk)
    context = {'project': project}
    return render(request, "base/project.html", context)



def blogPage(request,pk):
    blog = Blog.objects.get(id=pk)
    context = {'blog': blog}
    return render(request, "base/blog.html", context)



def addProject(request):
    
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/project_form.html', context)


def addBlog(request):
    
    Bform = BlogForm()

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if Bform.is_valid():
            form.save()
            return redirect('home')

    context = {'Bform': Bform}
    return render(request, 'base/blog_form.html', context)



def editProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/project_form.html', context)



def editBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    
    Bform = BlogForm(instance=blog)

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES,instance=blog)
        if Bform.is_valid():
            form.save()
            return redirect('home')

    context = {'Bform': Bform}
    return render(request, 'base/blog_form.html', context)

