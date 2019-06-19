from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404
import operator
import collections
import re

# Create your views here.
def main(request):
    return render(request, 'main.html')

def result(request):
    #Recupera o texto colocado no formulário.
    text_to_count = request.POST.get('text_to_count')

    #Transforma o texto capturado em letras minúsculas.
    text_to_count = text_to_count.lower()

    #Utiliza-se de expressão regular para remover todos os pontos, virgulas e caracteres indesejados.
    new_text_to_count = re.sub(u'[^a-z0-9àáéíóúçãõ: ]', ' ', text_to_count)
    
    #Cria um dicionário para armazenar a contagem das palavras.
    counts = dict()

    #Usa o split para separar os conjuntos de caracteres quando houver um espaço, caracterizando assim uma palavra.
    words = new_text_to_count.split()

    #Retorna o tamanho da lista que contem as palavras do texto, que é correspondente ao número de palavras do texto.
    words_quantity = len(words)

    #Realiza um for para cada palavra dentro da lista de palavras do texto.
    for word in words:

        #Verifica se já existe a palavra no dicionário de contagem, caso sim é adicionado mais um, caso contrário é adicionada a palvra.
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    #Ordena o dicionário com base nos valores, gerando assim uma tupla.
    counts = sorted(counts.items(), key=operator.itemgetter(1), reverse = True)

    #Reforma o dicionário para que seja enviado para a renderização.
    counts = collections.OrderedDict(counts)

    #Gera um dicionário com todos os elementos que devem ser enviados para a renderização.
    context = {'original_text': text_to_count, 'words_quantity': words_quantity, 'counts': counts}

    #Finaliza o código renderizando a interface final, passando o dicionário de valores.
    return render(request, 'result.html', context)