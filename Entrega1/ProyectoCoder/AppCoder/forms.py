from django import forms

class CursoFormulario(forms.Form):
    nombre = forms.CharField()
    comision=forms.IntegerField()
    fecha_creacion=forms.DateField()
    dia_semana=forms.IntegerField()

class ProductosFormulario(forms.Form):
    categoria = forms.CharField()
    rango_precio=forms.IntegerField()
   
class VendedoresFormulario(forms.Form):
    localidad=forms.CharField()
    tiempo_de_entrega=forms.IntegerField()
    calificacion=forms.IntegerField()