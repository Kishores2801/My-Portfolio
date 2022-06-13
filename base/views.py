from django.shortcuts import render, redirect
from .models import Project, Blog, Message
from .forms import  MessageForm, ProjectForm, BlogForm

from django.contrib import messages
   



def homepage(request):
    projects=Project.objects.all()
    blogs = Blog.objects.all()
    form = MessageForm()


    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'your Message is sucessfully sent')
    context={'projects': projects, "blogs":blogs, 'form':form}
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



def inboxPage(request):
    inbox=Message.objects.all().order_by("is_read")
    unreadCount =Message.objects.all().filter(is_read=False).count()
    context = {"inbox":inbox , 'unreadCount':unreadCount}
    return render(request, 'base/inbox.html', context)

    
def messagePage(request, pk):
    message=Message.objects.get(id=pk)
    context = {"message":message}
    message.is_read=True
    message.save()
    return render(request, 'base/messages.html', context)

