from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

# Register your models here.
#Todos los modelos que se registren aqui apareceran en el administrador del sitio de django 
#en http://direccion_del_sitio/admin/

class AlumnoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    class Meta:
        model = Alumno
        from_encoding= 'utf-8'

class MateriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    class Meta:
        model = Materia
        from_encoding= 'utf-8'

class GrupoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    class Meta:
        model = Grupo
        from_encoding= 'utf-8'

class TipoIncidenciaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    class Meta:
        model = tipoIncidencia
        from_encoding= 'utf-8'

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name' , 'last_name', 'email',)

class UserAdmin(UserAdmin):
    add_form = UserCreateForm
    prepopulated_fields = {'username': ('first_name' , 'last_name', )}

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'password1', 'password2', 'email',),
        }),
    )

admin.site.register(Especialidad)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Problematica)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(tipoIncidencia, TipoIncidenciaAdmin)
admin.site.register(Macros)
