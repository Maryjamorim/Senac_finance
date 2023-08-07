from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=50, null= False, blank=False, verbose_name='Categoria')
    essencial = models.BooleanField(default=False)
    valor_planejamento = models.FloatField(default=0, verbose_name='valor do planejamento')
    
    def __str__(self):
        return self.categoria
    
class Conta(models.Model):
    banco_choices = {
        ('NU',  'NUBANK'),
        ('CX',  'CAIXA'),
        ('IN',  'INTER'),
    }
    
    tipo_choices = {
        ('pf', 'Pessoa Física'),
        ('pj', 'Pessoa Jurídica'),
    }
    
    apelido = models.CharField(max_length=50)
    banco = models.CharField(max_length=3, choices= banco_choices)
    tipo = models.CharField(max_length=3, choices= tipo_choices)
    valor = models.FloatField(verbose_name='Valor do deposito')
    icone = models.ImageField(upload_to='Icone', verbose_name='Icone do banco')
    
    
    def __str__(self):
        return self.apelido