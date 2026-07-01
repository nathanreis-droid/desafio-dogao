from django.shortcuts import redirect, render

from clientes.forms import ClientForm
from clientes.models import Client
from django.views.generic.list import ListView
from django.views.generic import UpdateView,CreateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from api.cliente import get_cliente

# Create your views here.
@method_decorator(login_required(login_url='login'),name='dispatch') 
class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'
    context_object_name = 'client_list'
    
    def get_queryset(self):
        
        cliente = super().get_queryset().order_by('fantasy_name')
        search = self.request.GET.get('search')
        
        if search:
            cliente = cliente.filter(fantasy_name__icontains=search)
        return cliente
    
@method_decorator(login_required(login_url='login'),name='dispatch') 
class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'client_update.html'
    success_url = '/client_list/'
@method_decorator(login_required(login_url='login'),name='dispatch') 
class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'client_new.html'
    success_url = '/client_list/'
@method_decorator(login_required(login_url='login'),name='dispatch') 
class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = '/client_list/'


##@method_decorator(login_required(login_url='login'),name='dispatch') 
def sicronize_view(request):
    
    clientes_api =    get_cliente()["cliente"]
    
    for item in range(len(clientes_api)):
        # new_client = Client(
        #                             type =["A1_PESSOA"],
        #                             company_name =["A1_NOME"],
        #                             fantasy_name =clientes_api[item]["A1_NREDUZ"],
        #                             email =clientes_api[item]["A1_EMAIL"]
        #                         )
        valores_api = {
                                'type': clientes_api[item]['A1_PESSOA'],
                                'company_name': clientes_api[item]['A1_NOME'],
                                'fantasy_name': clientes_api[item]['A1_NREDUZ'],
                                'representative': '4',
                                'email':'email@teste.com' if clientes_api[item]["A1_EMAIL"] == '' else clientes_api[item]["A1_EMAIL"] 
                            }
        new_client = ClientForm(data=valores_api)

        if new_client.is_valid():
            new_client.save()
            
        else: 
            print(valores_api)

    return redirect('client_list')
        

