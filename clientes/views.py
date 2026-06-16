from django.shortcuts import render

from clientes.forms import ClientForm
from clientes.models import Client
from django.views.generic.list import ListView
from django.views.generic import UpdateView,CreateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

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
