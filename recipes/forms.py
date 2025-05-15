from django import forms
from .models import Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['nombre', 'descripcion', 'instrucciones']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError("El nombre de la receta es obligatorio.")
        return nombre

    # Validación para las instrucciones (asegurarse de que tengan al menos 5 palabras)
    def clean_instrucciones(self):
        instrucciones = self.cleaned_data.get('instrucciones')
        if len(instrucciones.split()) < 5:  # Al menos 5 palabras
            raise forms.ValidationError("Las instrucciones deben ser más detalladas.")
        return instrucciones