"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import login_view, logout_view, register_view
from clientes.views import ClientUpdateView, ClientCreateView,ClientDeleteView
from clientes.views import ClientListView,sicronize_view
from vendedores.views import RepresentativeListView,RepresentativeUpdateView,RepresentativeCreateView,RepresentativeDeleteView, sicronize_representant_view
urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('login/', login_view,name='login'),
    path('logout/', logout_view,name='logout'),
    path('register/', register_view,name='register'),
    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('client_new/', ClientCreateView.as_view(),name='client_new'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(),name='client_update'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(),name='client_delete'),
    path('representative_list/', RepresentativeListView.as_view(), name='representative_list'),
    path('representative_new/', RepresentativeCreateView.as_view(), name='representative_new'),
    path('representative_update/<int:pk>/', RepresentativeUpdateView.as_view(), name='representative_update'),
    path('representative_delete/<int:pk>/', RepresentativeDeleteView.as_view(),name='representative_delete'),
    path('cliente_sicroniza/', sicronize_view ,name='cliente_sicroniza'),
    path('representative_sicroniza/', sicronize_representant_view ,name='representative_sicroniza'),

]
