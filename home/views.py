import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Reserva

def home(request):
    return render(request, 'index.html')

@csrf_exempt
def cadastrar_reserva(request):
    if request.method != 'POST':
        return JsonResponse({'erro': 'Método não permitido'}, status=405)

    try:
        dados = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'erro': 'JSON inválido'}, status=400)

    nome = dados.get('nome_completo')
    data_hora = dados.get('data_horario')
    quantidade = dados.get('quantidade_pessoas')

    if not nome or not data_hora or not quantidade:
        return JsonResponse({'erro': 'Todos os campos são obrigatórios'}, status=400)

    reserva = Reserva.objects.create(
        nome_completo=nome,
        data_horario=data_hora,
        quantidade_pessoas=quantidade
    )

    return JsonResponse({'mensagem': 'Reserva realizada com sucesso!', 'id': reserva.id}, status=201)