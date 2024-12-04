import qrcode
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Veiculo
from .forms import RegistroUsoForm

def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'veiculos/lista_veiculos.html', {'veiculos': veiculos})

def gerar_qr_code(request, veiculo_id):
    ip_local = "192.168.0.73"  # Substitua pelo seu IP local
    url = f"http://{ip_local}:8000/veiculos/veiculo/{veiculo_id}/"

    qr = qrcode.make(url)
    response = HttpResponse(content_type="image/png")
    qr.save(response, "PNG")
    return response


from django.shortcuts import redirect

from django.shortcuts import redirect

from django.shortcuts import render, get_object_or_404, redirect
from .models import Veiculo
from .forms import RegistroUsoForm

def registrar_uso(request, veiculo_id):
    veiculo = get_object_or_404(Veiculo, id=veiculo_id)

    if request.method == 'POST':
        form = RegistroUsoForm(request.POST)
        if form.is_valid():
            print("Formulário válido. Dados:", form.cleaned_data)  # Depuração para validar dados do formulário
            registro = form.save(commit=False)
            registro.veiculo = veiculo
            registro.save()
            return redirect('sucesso', veiculo_id=veiculo.id)  # Certifique-se do nome correto da URL
        else:
            print("Formulário inválido. Erros:", form.errors)  # Depuração para verificar erros do formulário
    else:
        form = RegistroUsoForm()

    return render(request, 'veiculos/registro_uso.html', {
        'form': form,
        'veiculo': veiculo,
    })


def sucesso(request, veiculo_id):
    veiculo = get_object_or_404(Veiculo, id=veiculo_id)
    return render(request, 'veiculos/sucesso.html', {'veiculo': veiculo})


