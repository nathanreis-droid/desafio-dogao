from django.shortcuts import render

from vendedores.models import Representative
from django.views.generic import UpdateView,ListView,CreateView,DeleteView
from vendedores.forms import RepresentativeForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.


@method_decorator(login_required(login_url='login'),name='dispatch') 
class RepresentativeListView(ListView):
    model = Representative
    template_name = 'representative_list.html'
    context_object_name = 'representative_list'
    
    def get_queryset(self):
        
        vendedor = super().get_queryset().order_by('name')
        search = self.request.GET.get('search')
        
        if search:
            vendedor = vendedor.filter(name__icontains=search)
        return vendedor
    
@method_decorator(login_required(login_url='login'),name='dispatch') 
class RepresentativeUpdateView(UpdateView):
    model = Representative
    form_class = RepresentativeForm
    template_name = 'representative_update.html'
    success_url ='/representative_list/'

@method_decorator(login_required(login_url='login'),name='dispatch')
class RepresentativeCreateView(CreateView):
    model = Representative
    form_class = RepresentativeForm
    template_name = 'representative_new.html'
    success_url ='/representative_list/'

@method_decorator(login_required(login_url='login'),name='dispatch')
class RepresentativeDeleteView(DeleteView):
    model = Representative
    template_name = 'representative_delete.html'
    success_url ='/representative_list/'