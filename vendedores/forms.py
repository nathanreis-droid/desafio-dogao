from django import forms

from vendedores.models import Representative 

class RepresentativeForm(forms.ModelForm):

    class Meta:
        model = Representative
        fields = '__all__' 