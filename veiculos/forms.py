from django import forms
from .models import RegistroUso

class RegistroUsoForm(forms.ModelForm):
    class Meta:
        model = RegistroUso
        fields = ['nome_usuario', 'kilometragem_saida', 'kilometragem_chegada', 'destino', 'horario_saida', 'horario_chegada']
    
    # Defina as validações se necessário, mas normalmente o Django já fará isso para DateTimeField
