from django.db import models

# Create your models here.

class Representative(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,verbose_name='Nome')
    birth = models.DateField(blank=True,null= True,verbose_name='Nascimento')
    email = models.EmailField(max_length=254,verbose_name='E-mail')
    salary = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Salario')
    activate = models.BooleanField(blank=False,null= False,verbose_name='Status')

    def __str__(self):
        return self.name