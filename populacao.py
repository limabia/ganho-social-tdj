# coding=utf-8
# generate random integer values
from random import seed
from random import randint
import random


class Jogador:
    """ Classe que define o conjunto de argumentos que cada player tem"""
    perfil: str
    conteudo_interesse = []
    conteudo_publicado = []
    qualidade_publicacao: float
    frequencia_publicacao: float
    utilidade = 0.0
    minimoConsumo = 0.0
    segue = []
    seguidores = []

    def __init__(self, perfil, conteudo_interesse, conteudo_publicado, qualidade_publicacao, frequencia_publicacao, minimo_consumo):
        self.perfil = perfil
        self.conteudo_interesse = conteudo_interesse
        self.conteudo_publicado = conteudo_publicado
        self.qualidade_publicacao = float(qualidade_publicacao)
        self.frequencia_publicacao = float(frequencia_publicacao)
        self.minimoConsumo = float(minimo_consumo)


def gera_qualidade(faixa_qualidade):
    if(faixa_qualidade == 'alta'):
        return random.uniform(0.7, 0.99)
    if(faixa_qualidade == 'media'):
        return random.uniform(0.3, 0.7)
    if(faixa_qualidade == 'baixa'):
        return random.uniform(0, 0.3)

def gera_frequencia(faixa_frequencia):
    if(faixa_frequencia == 'alta'):
        return random.uniform(0.7, 0.99)
    if(faixa_frequencia == 'media'):
        return random.uniform(0.3, 0.7)
    if(faixa_frequencia == 'baixa'):
        return random.uniform(0, 0.3)

def gera_conteudo(faixa_conteudo):
    tipos_conteudo = ['comida','meme','atividades','selfies','fotos_em_grupo']
    conteudo_aleatorio = []

    if(faixa_conteudo == 'alta'):
        return tipos_conteudo
    if(faixa_conteudo == 'media'):
        i = randint(3, 4)
        for x in range(i):
            randomIndex = randint(0, len(tipos_conteudo) - 1)
            while tipos_conteudo[randomIndex] in conteudo_aleatorio:
                randomIndex = randint(0, len(tipos_conteudo) - 1)
            conteudo_aleatorio.append(tipos_conteudo[randomIndex])
        return conteudo_aleatorio
    if(faixa_conteudo == 'baixa'):
        i = randint(1, 2)
        for x in range(i):
            randomIndex = randint(0, len(tipos_conteudo) - 1)
            while tipos_conteudo[randomIndex] in conteudo_aleatorio:
                randomIndex = randint(0, len(tipos_conteudo) - 1)
            conteudo_aleatorio.append(tipos_conteudo[randomIndex])
        return conteudo_aleatorio
    

def gera_limiar(faixa_limiar):
    if(faixa_limiar == 'alta'):
        return random.uniform(0.7, 0.99)
    if(faixa_limiar == 'media'):
        return random.uniform(0.3, 0.7)
    if(faixa_limiar == 'baixa'):
        return random.uniform(0, 0.3)
        

def gera_jogador(atributos):
    interesse = gera_conteudo(atributos[1])
    publicado = gera_conteudo(atributos[2])
    qualidade = gera_qualidade(atributos[3])
    frequencia = gera_frequencia(atributos[4])
    limiar = gera_limiar(atributos[5])

    jogador = Jogador(
        perfil=atributos[0],
        conteudo_interesse=interesse,
        conteudo_publicado=publicado,
        qualidade_publicacao=qualidade,
        frequencia_publicacao=frequencia,
        minimo_consumo=limiar
    )
    return jogador


def gera_getalhes(pathFile):
    fileOpen = open(pathFile, "r")
    lista = []
    if fileOpen.mode == 'r':
        contents = fileOpen.readlines()
        while contents:
            linha = contents.pop().replace("\n", "")
            atributos = linha.split(",")
            lista.append(atributos)
    fileOpen.close()
    return lista


def gera_populacao(tipo_perfis, detalhes_pop):
    populacao = []
    total_pop = 0

    lista_perfis = gera_getalhes(tipo_perfis)
    lista_detalhes_pop = gera_getalhes(detalhes_pop)

    perfil_dict = {}

    for perfil in lista_perfis:
        perfil_dict[perfil[0]] = perfil

    for detalhe_pop in lista_detalhes_pop:
        if(detalhe_pop[0] == 'pop'):
            total_pop = int(detalhe_pop[1])

        if(detalhe_pop[0] in perfil_dict):
            qtd_perfil1 = int(detalhe_pop[1])
            for i in range(qtd_perfil1):
                populacao.append(gera_jogador(perfil_dict[detalhe_pop[0]]))
            total_pop -= qtd_perfil1

    # TODO arrumar esse total pop para nao criar coisa que nao deve
    #for i in range(total_pop):
    #    populacao.append(gera_jogador_aleatorio(lista_perfis))

    return populacao
