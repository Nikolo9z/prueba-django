from django.shortcuts import render, redirect
from .models import Estacionamiento

# Create your views here.
def datos(request):
    estacionamientos=Estacionamiento.objects.all()
    return render(request,"index.html",{"Estacionamientos":estacionamientos})

def RegistrarVehiculo(request):
    piso=request.POST['pisos']
    telefono=request.POST['telefono']
    
    esta=Estacionamiento.objects.create(piso=piso,telefono=telefono)
    return redirect('/')