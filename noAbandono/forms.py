from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import *

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = '__all__'

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = '__all__'

class ProblematicaForm(forms.ModelForm):
    class Meta:
        model = Problematica
        fields = '__all__'
