from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import FilmesForm,SerieForm
from app.models import Filmes,Serie
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
    return render(request, 'index.html', data)


def homeSerie(request):
    data1 = {}
    search =request.GET.get('search')
    if search:
        data1['db1'] = Serie.objects.filter(modelo__icontains=search)
    else:
        data1['db1'] = Serie.objects.all()

    return render(request, 'verSerie.html', data1)


def form(request):
    data = {}
    data['form'] = FilmesForm
    return render(request, 'form.html', data)


def formSerie(request):
    data1 = {}
    data1['formSerie'] = SerieForm
    return render(request, 'adserie.html', data1)

def createSerie(request):
    formSerie = SerieForm(request.POST)
    if formSerie.is_valid():
        formSerie.save()
        return redirect('home')


def create(request):
    form = FilmesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Filmes.objects.get(pk=pk)
    return render(request, 'view.html', data)

def viewSerie(request, pk):
    data1 = {}
    data1['db1'] = Serie.objects.get(pk=pk)
    return render(request, 'viewSerie.html', data1)


def editSerie(request, pk):
    data = {}
    data['db1'] = Serie.objects.get(pk=pk)
    data['formSerie'] = SerieForm(instance=data['db1'])
    return render(request, 'adserie.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Filmes.objects.get(pk=pk)
    data['form'] = FilmesForm(instance=data['db'])
    return render(request, 'form.html', data)

def updateSerie(request, pk):
    data = {}
    data['db1'] = Serie.objects.get(pk=pk)
    formSerie = SerieForm(request.POST or None, instance=data['db1'])
    if formSerie.is_valid():
        formSerie.save()
        return redirect('home')

def update(request, pk):
    data = {}
    data['db'] = Filmes.objects.get(pk=pk)
    form = FilmesForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def deleteSerie(request, pk):
    db1 =  Serie.objects.get(pk=pk)
    db1.delete()
    return redirect('home')

def delete(request, pk):
    db =  Filmes.objects.get(pk=pk)
    db.delete()
    return redirect('home')