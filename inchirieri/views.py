from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, LoginForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # schimbă cu pagina principală
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

from django.http import HttpResponse

from .models import Car

def home_view(request):
    masini = Car.objects.all()

    # Extrage filtrele din GET
    pret_min = request.GET.get('pret_min')
    pret_max = request.GET.get('pret_max')
    an_min = request.GET.get('an_min')
    an_max = request.GET.get('an_max')

    # Aplică filtrele dacă există valori
    if pret_min:
        masini = masini.filter(pret__gte=pret_min)
    if pret_max:
        masini = masini.filter(pret__lte=pret_max)
    if an_min:
        masini = masini.filter(an_fabricatie__gte=an_min)
    if an_max:
        masini = masini.filter(an_fabricatie__lte=an_max)

    return render(request, 'home.html', {
        'masini': masini
    })


from django.contrib.auth.decorators import login_required
from .forms import MasinaForm

@login_required
def adauga_masina(request):
    if request.user.account_type != 'owner':
        return redirect('home')  # doar proprietarii pot adăuga mașini

    if request.method == 'POST':
        form = MasinaForm(request.POST,request.FILES)
        if form.is_valid():
            masina = form.save(commit=False)
            masina.dealer = request.user
            masina.save()
            return redirect('home')
    else:
        form = MasinaForm()

    return render(request, 'adauga_masina.html', {'form': form})

from .models import Car, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

@login_required
def adauga_recenzie(request, car_id):
    masina = Car.objects.get(pk=car_id)

    if request.user.account_type != 'renter':
        return redirect('home')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            recenzie = form.save(commit=False)
            recenzie.user = request.user
            recenzie.car = masina
            recenzie.save()
            return redirect('home')
    else:
        form = ReviewForm()

    return render(request, 'adauga_recenzie.html', {'form': form, 'masina': masina})

from django.shortcuts import get_object_or_404
from django.contrib import messages

@login_required
def editeaza_masina(request, car_id):
    masina = get_object_or_404(Car, pk=car_id, dealer=request.user)

    if request.method == 'POST':
        form = MasinaForm(request.POST, request.FILES, instance=masina)
        if form.is_valid():
            form.save()
            messages.success(request, "Mașina a fost actualizată.")
            return redirect('home')
    else:
        form = MasinaForm(instance=masina)

    return render(request, 'editeaza_masina.html', {'form': form, 'masina': masina})


@login_required
def sterge_masina(request, car_id):
    masina = get_object_or_404(Car, pk=car_id, dealer=request.user)
    if request.method == 'POST':
        masina.delete()
        messages.success(request, "Mașina a fost ștearsă.")
        return redirect('home')
    return render(request, 'sterge_masina.html', {'masina': masina})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Car, CarRented, Review

@login_required
def despre_utilizator(request):
    user = request.user
    masini_inchiriate = CarRented.objects.filter(utilizator=user)
    recenzii = Review.objects.filter(user=user)
    masini_proprii = Car.objects.filter(dealer=user)

    return render(request, 'despre_utilizator.html', {
        'masini_inchiriate': masini_inchiriate,
        'recenzii': recenzii,
        'masini_proprii': masini_proprii,
    })

@login_required
def inchiriaza_masina(request, masina_id):
    masina = get_object_or_404(Car, id=masina_id)
    CarRented.objects.create(masina=masina, utilizator=request.user)
    return redirect('despre_utilizator')

@login_required
def elimina_inchiriere(request, inchiriere_id):
    inchiriere = get_object_or_404(CarRented, id=inchiriere_id, utilizator=request.user)
    inchiriere.delete()
    messages.success(request, "Mașina a fost eliminată din lista ta de închirieri.")
    return redirect('despre_utilizator')

from django.contrib.admin.views.decorators import staff_member_required
from .models import Review

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Review

@login_required
def sterge_recenzie(request, recenzie_id):
    recenzie = get_object_or_404(Review, id=recenzie_id)

    # Verificăm dacă utilizatorul curent este autorul recenziei
    if recenzie.user != request.user:
        messages.error(request, "Nu ai permisiunea să ștergi această recenzie.")
        return redirect('despre_utilizator')

    if request.method == 'POST':
        recenzie.delete()
        messages.success(request, "Recenzia a fost ștearsă cu succes.")
        return redirect('despre_utilizator')

    # Dacă vrei, poți adăuga o pagină de confirmare sau poți redirecta
    return redirect('despre_utilizator')




