from django.shortcuts import render, redirect, get_object_or_404
from .models import Receta
from .forms import RecetaForm

# Vista para listar las recetas
def listar_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'recipes/listar_recetas.html', {'recetas': recetas})


# Vista para ver una receta individual
def ver_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    return render(request, 'recipes/ver_receta.html', {'receta': receta})

# Vista para crear una nueva receta
def crear_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_recetas')
    else:
        form = RecetaForm()
    return render(request, 'recipes/crear_receta.html', {'form': form})


# Vista para eliminar una receta
def eliminar_receta(request, receta_id):
    receta = Receta.objects.get(id=receta_id)
    receta.delete()
    return redirect('listar_recetas')