from django.contrib import admin
from clientes.models import Client

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display =('company_name','fantasy_name','type','email','representative','create_date')
    search_fields = ('fantasy_name',)
admin.site.register(Client,ClienteAdmin)