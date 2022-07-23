from django.contrib import admin

from .models import Chassi, Carro, Montadora

@admin.register(Montadora)
class MontadoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Chassi)
class ChassiAdmin(admin.ModelAdmin):
    list_display = ('numero', ) # a virgula diz que é uma tupla


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('montadora', 'modelo', 'chassi', 'preco', 'get_motoristas')
    """ motoristas é um relacionamento entre os usuários e os carros, 
    não é possível a exibição direta, porisso é criada a função get_motoristas"""

    def get_motoristas(self, obj):
        """Usa a list compreenshion para exibição da lista no admin"""
        return ', '.join([m.username for m in obj.motoristas.all()])

    get_motoristas.short_description = 'Motoristas'
    """ define o nome a ser exibito no adim, sem esse método apareceria o nome da função: get_motoristas"""