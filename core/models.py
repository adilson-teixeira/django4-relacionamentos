from django.db import models
from django.contrib.auth import get_user_model


class Chassi(models.Model): #Entidade forte (sem chaves estrangeiras)
    numero = models.CharField('Chassi', max_length=16, help_text='Máximo 16 caractéres')

    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural = 'Chassis'

    def __str__(self):
        return self.numero


class Montadora(models.Model): #Entidade forte (sem chaves estrangeiras)
    nome = models.CharField('Nome', max_length=50)

    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'

    def __str__(self):
        return self.nome


def set_default_montadora():#pode ser qualquer nome.
    """devolve (objeto, boolean), objeto criado (boolean True) ou existente (boolean False)
    return Montadora.objects.get_or_create(nome='Padrao')"""
    return Montadora.objects.get_or_create(nome='Não cadastrada')[0] #o [0] faz devolver apenas o nome sem o booleano
 

class Carro(models.Model): 
    #Entidade fraca - chaves entrangeiras de Montadoras e motoristas (User) get_user_model()
    # OneToOneField ( chassi)
    """Relacionamento OneToOneField  um para um cada carro só pode se relacionar com um chassi e cada chassi só com um carro é possível recuperar a partir de qualquer um dos dados Chassi => carro, Carro => Chassi e seus respectivos atributos"""
    # ForeignKey - One to Many (montadora)
    """Cada carro tem uma montadora, mas uma montadora pode 'montar' vários carros
     carros = montadora.carro_set.all() retorna os carros vinculados"""
    # ManuToMany (motorista) - Relecionamento entre tabelas
    """Um carro pode ser dirigido por vários motoristas e um motorista pode dirigir vários carros"""
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)
    #montadora = models.ForeignKey(Montadora, on_delete=models.CASCADE)
    #montadora = models.ForeignKey(Montadora, on_delete=models.SET_DEFAULT, default=1)
    montadora = models.ForeignKey(Montadora, on_delete=models.SET(set_default_montadora))#Função definida antes da classe
    """Colocando um opção default para não deletar em castaca"""
    motoristas = models.ManyToManyField(get_user_model())
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    modelo = models.CharField('Modelo', max_length=30, help_text='Máximo 30 caractéres')

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f'{self.montadora} {self.modelo}'

