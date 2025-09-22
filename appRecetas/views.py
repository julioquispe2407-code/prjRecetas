from django.shortcuts import render, get_object_or_404, redirect
from .models import Receta
from .forms import RecetaForm
from django.core.management import call_command
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
# Vista para la lista de recetas
def lista_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'recetas/lista.html', {'recetas': recetas})

# Vista para los detalles de una receta
def detalle_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    return render(request, 'recetas/detalle.html', {'receta': receta})

# Vista para el formulario de nueva receta
def nueva_receta(request):
    if request.method == "POST":
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            receta = form.save(commit=False)
            receta.save()
            return redirect('detalle_receta', pk=receta.pk)
    else:
        form = RecetaForm()
    return render(request, 'recetas/nueva.html', {'form': form})
def run_migrations(request):
    if not settings.DEBUG:
        call_command('migrate')
        return HttpResponse("Migrations applied successfully!")
    return HttpResponse("Migrations can only be run in production.", status=403)