from django.shortcuts import render
import locale
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'calculadora/index.html' )

def calcularFemininoMasculino(request):
    if request.method == 'POST':
        peso = float(request.POST.get('peso', 0)) #vai estar salvando oq é enviado lá campo do peso no post do index
        altura = float(request.POST.get('altura', 0))
        
        resultadoIMC = resultado_imc(peso, altura)
        
        return render(request, 'calculadora/escolhaHomemMulher.html',{'resultado': resultadoIMC})
    return HttpResponse('Requisição Inválida')
        
def resultado_imc(peso, altura):
    if altura > 0:
        resultado = peso/(altura**2)
        return resultado
    return 0

def resultadoHM(request):
    if request.method == 'POST':
        genero = request.POST.get('genero') #get é sempre no name do item do forms
        resultado=float(request.POST.get('resultado', 0))
        
        msg = ''
        recomenda = ''
        if genero == 'homem':
        
            if resultado <= 20:
                msg = 'o peso Abaixo do Normal'
                recomenda = 'coma mais'
            elif resultado > 20 and resultado <= 25:
                msg = 'o peso Normal'
                recomenda = 'mantenha a dieta'
            elif resultado > 25 and resultado <= 30:
                msg = 'Obesidade Leve'
                recomenda = 'faça exercícios'
            elif resultado > 30 and resultado <= 40:
                msg = 'Obesidade Moderada'
                recomenda = 'procure um nutricionista'
            elif resultado > 40:
                msg = 'Obesidade Mórbida'
                recomenda = 'consulte-se com um médico urgentemente'

        elif genero == 'mulher':
           
            if resultado <= 19:
                msg = 'o peso Abaixo do Normal'
                recomenda = 'coma mais'
            elif resultado > 19 and resultado <= 24:
                msg = 'o peso Normal'
                recomenda = 'mantenha a dieta'
            elif resultado > 24 and resultado <= 29:
                msg = 'Obesidade Leve'
                recomenda = 'faça exercícios'
            elif resultado > 29 and resultado <= 39:
                msg = 'Obesidade Moderada'
                recomenda = 'procure um nutricionista'
            elif resultado > 39:
                msg = 'Obesidade Mórbida'
                recomenda = 'consulte-se com um médico urgentemente'

        # Renderiza a página de resultado
        resultado = resultadoFormatado(resultado)
        return render(request, 'calculadora/resultadoPorSexo.html', {'msg': msg, 'recomenda': recomenda, 'resultado': resultado})
    
    return HttpResponse('Requisição Inválida')
        
def resultadoFormatado (resultado):
    if isinstance(resultado, float):
        return locale.format_string('%.2f', resultado, grouping=True)
    return resultado