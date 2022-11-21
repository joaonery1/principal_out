from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import FilmesForm
from app.models import Filmes
# Create your views here.
# Create your views here.
# Create your views here
# 
# 
def home(request):
    data = {}
    search =request.GET.get('search')
    if search:
        data['db'] = Filmes.objects.filter(modelo__icontains=search)
    else:
        data['db'] = Filmes.objects.all()

    #data['db'] = Carros.objects.all()
    #all = Carros.objects.all()
    #paginator = Paginator(all,2)
    #pages = request.GET.get('page')
    #data['db']= paginator.get_page(pages)

    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = FilmesForm
    return render(request, 'form.html', data)

def create(request):
    form = FilmesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Filmes.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Filmes.objects.get(pk=pk)
    data['form'] = FilmesForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Filmes.objects.get(pk=pk)
    form = FilmesForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db =  Filmes.objects.get(pk=pk)
    db.delete()
    return redirect('home')