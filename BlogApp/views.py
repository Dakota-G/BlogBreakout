from django.shortcuts import render, redirect
from .models import *

# Create your views here.

# RENDER VIEWS:
def index(request):
    context = {
        "all_users": User.objects.all()
    }
    return render(request, "index.html", context)

def all_blogs(request):
    context = {
        "all_blogs": Blog.objects.all(),
        "all_users": User.objects.all()
    }
    return render(request, "blogs.html", context)

def one_blog(request, blog_id):
    context = {
        "pineapple": Blog.objects.get(id = blog_id)
    }
    return render(request, "view_blog.html", context)

def blog_editor(request, blog_id):
    context = {
        "blog_to_edit": Blog.objects.get(id = blog_id)
    }
    return render(request, "blog_editor.html", context)

# REDIRECTS

def create_user(request):
    User.objects.create(Username = request.POST['username'])
    return redirect('/')

def create_blog(request):
    user = User.objects.get(id = request.POST['creator'])
    Blog.objects.create(Title = request.POST['title'], Text=request.POST['content'], Creator = user)
    return redirect('/blogs')

def edit_blog(request, blog_id):
    blog = Blog.objects.get(id = blog_id)
    blog.Title = request.POST['title']
    blog.Text = request.POST['content']
    blog.save()
    return redirect(f'/blogs/{blog_id}')

def delete_blog(request, blog_id):
    blog = Blog.objects.get(id = blog_id)
    blog.delete()
    return redirect('/blogs')

