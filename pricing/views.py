from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def home(request):
    return render(request, 'home.html')

@login_required
def meu_hotel(request):
    user = request.user
    try:
        hotel = Hotel.objects.get(user=user)
    except Hotel.DoesNotExist:
        hotel = None

    if request.method == 'POST':
        form = HotelForm(request.POST, instance=hotel)
        if form.is_valid():
            hotel = form.save(commit=False)
            hotel.user = user
            hotel.save()
            return redirect('home')
    else:
        form = HotelForm(instance=hotel)
    
    return render(request, 'meu_hotel.html', {'form': form, 'hotel': hotel})

@login_required
def visualizar_calendario(request):
    hotel = Hotel.objects.get(user=request.user)
    return render(request, 'calendario.html')

@login_required
def adicionar_quarto(request):
    if request.method == 'POST':
        form = TipoQuartoForm(request.POST)
        if form.is_valid():
            quarto = form.save(commit=False)
            quarto.hotel = Hotel.objects.get(user=request.user)
            quarto.save()
            return redirect('quartos')
    else:
        form = TipoQuartoForm()
    return render(request, 'adicionar_quarto.html', {'form': form})

@login_required
def lista_quartos(request):
    hotel = Hotel.objects.get(user=request.user)
    quartos = TipoQuarto.objects.filter(hotel=hotel)
    return render(request, 'quartos.html', {'quartos': quartos})
