from django.shortcuts import render, redirect
from django.views import generic
from .models import (
        Blog,
        Review,
        TuBlog
    )
from main.forms import BlogCreate, CreateUserForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


class IndexView(generic.TemplateView): #Vista principal
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blogs = Blog.objects.filter(is_active=True)
        context["blogs"] = blogs
        return context
        
def CrearBlog(request): #Función para crear y guardar los blogs 
    form = None
    if request.method=="POST":
        form = BlogCreate(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, "main/indexBlog.html",{"form":form})


def reviews(request): #Función para crear y guardar los comentarios 
    Nombre = request.POST['name']
    descripcion = request.POST['description']
    texto = request.POST['body']

    cr = Review.objects.create(name = Nombre, description=descripcion, body=texto)
    return redirect('/')

class ReviewView(generic.TemplateView): #Vista de la zona de comentarios 
    template_name = "main/indexReview.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review = Review.objects.filter(is_active=True)
        context["review"] = review
        return context

class BlogView(generic.TemplateView): #Vista de zona de creacion de blog
    template_name = "main/indexBlog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tublog = TuBlog.objects.filter(is_active=True)
        context["tublog"] = tublog
        return context

def loginPage(request):
    if request.user.is_authenticated:  #Si el usuario existe lo manda a la pagina principal
        return redirect('/')
    else:  
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username or password incorrect') #Error por si las credenciales no existen o son incorrectas

        context = {}
        return render(request, 'main/indexLogin.html', context)

def registerPage(request): #Función para crear un usuario
    if request.user.is_authenticated: 
        return redirect('main:home') 
    else: 
        form = CreateUserForm() 
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was craeted for')

                return redirect('main:home')
        context = {'form':form}
        return render(request, 'main/indexRegister.html', context)

def logoutUser(request): #Cierre de sesion
    logout(request)
    return redirect('/')