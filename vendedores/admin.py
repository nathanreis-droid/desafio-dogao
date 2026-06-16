from django.contrib import admin

from vendedores.models import Representative

# Register your models here.
class VerAdmin(admin.ModelAdmin):
    list_display =('name','birth','email','salary','activate')
    search_fields = ('name',)

admin.site.register(Representative,VerAdmin)