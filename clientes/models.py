from django.db import models

from vendedores.models import Representative
from datetime import date
# Create your models here.



class People(models.TextChoices):
    JURIDIC = 'J', ('Pessoa juridica')
    FISICA = 'F', ('Pessoa Fisica')
    
class Client(models.Model):

    id = models.AutoField(primary_key=True)
    type = models.CharField(choices=People.choices, max_length=1, blank=False,null=False,verbose_name='Tipo')
    company_name = models.CharField(max_length=100,verbose_name='Razão Social',null=False,blank=False)
    fantasy_name = models.CharField(max_length=50,verbose_name='Nome Fantasia')
    create_date = models.DateField(auto_now_add=True,default=date.today(),verbose_name='Data de abertura')
    email = models.EmailField(max_length=254,verbose_name='E-mail' )
    representative = models.ForeignKey(Representative, on_delete=models.PROTECT,related_name='people',verbose_name='Vendedor',limit_choices_to={'activate': True})