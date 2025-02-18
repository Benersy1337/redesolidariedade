import re
from django import forms
from django.utils.translation import gettext as _
from .models import Familia, IntegranteFamilia

#------------------------------------------------------------------------------
#FORMULARIOS FAMILIAS
#------------------------------------------------------------------------------

#FORMULARIO FAMILIAS
class FamiliaForm(forms.ModelForm):

    def clean_nomeChefeFamilia(self):
      nomeChefeFamilia = self.cleaned_data['nomeChefeFamilia']
      nomeChefeFamilia = re.sub(' -- CPF:', '', nomeChefeFamilia)
      return nomeChefeFamilia

    def clean_cpfChefeFamilia(self):
        cpfChefeFamilia = self.cleaned_data['cpfChefeFamilia']
        cpfChefeFamilia = re.sub('[^0-9]', '', cpfChefeFamilia)
        if (cpfChefeFamilia == ""):
            return cpfChefeFamilia
        if Familia.objects.filter(cpfChefeFamilia = cpfChefeFamilia).exists():
            raise forms.ValidationError(_('CPF em Uso!'))
        return cpfChefeFamilia

    class Meta:
        model = Familia
        labels = {
          "nomeChefeFamilia": "Nome",
          "cpfChefeFamilia": "CPF",
          "enderecoChefeFamilia": "Endereço",
        }
        fields = "__all__"

#FORMULARIO EDITAR FAMILIA
class EditFamiliaForm(forms.ModelForm):

    class Meta:
        model = Familia
        labels = {
          "nomeChefeFamilia": "Nome do chefe da família",
          "cpfChefeFamilia": "CPF do chefe da família",
          "enderecoChefeFamilia": "Endereço",
        }
        fields = "__all__"
        exclude = ['cpfChefeFamilia']

#FORMULARIO INTEGRANTES DE FAMILIA
class IntegranteFamiliaForm(forms.ModelForm):

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        cpf = re.sub('[^0-9]', '', cpf)
        return cpf

    class Meta:
        model = IntegranteFamilia
        labels = {
          "familia": "Família de",
          "nome": "Nome",
          "cpf": "CPF"
        }
        fields = "__all__"

#------------------------------------------------------------------------------