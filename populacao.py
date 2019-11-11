# coding=utf-8
# generate random integer values
from random import seed
from random import randint


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
        self.conteudo_interesse = conteudo_interesse.split(";")
        self.conteudo_publicado = conteudo_publicado.split(";")
        self.qualidade_publicacao = float(qualidade_publicacao)
        self.frequencia_publicacao = float(frequencia_publicacao)
        self.minimoConsumo = float(minimo_consumo)



def gera_jogador(atributos):
    jogador = Jogador(
        perfil=atributos[0],
        conteudo_interesse=atributos[1],
        conteudo_publicado=atributos[2],
        qualidade_publicacao=atributos[3],
        frequencia_publicacao=atributos[4],
        minimo_consumo=atributos[5]
    )
    return jogador


def gera_jogador_aleatorio(lista_atributos):
    # seed random number generator
    seed(1)
    randomIndex = randint(0, len(lista_atributos))
    atributos = lista_atributos[randomIndex]
    return gera_jogador(atributos)


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

    lista_detalhes_pop = gera_getalhes(detalhes_pop)
    lista_perfis = gera_getalhes(tipo_perfis)

    for perfil in lista_perfis:
        if(perfil[0] == 'perfil1'):
            perfil1 = detalhe_pop[1]
        if(perfil[0] == 'perfil2'):
            perfil2 = detalhe_pop[1]
        if(perfil[0] == 'perfil3'):
            perfil3 = detalhe_pop[1]
        if(perfil[0] == 'perfil4'):
            perfil4 = detalhe_pop[1]

    for detalhe_pop in lista_detalhes_pop:
        if(detalhe_pop[0] == 'pop'):
            total_pop = detalhe_pop[1]

        if(detalhe_pop[0] == 'perfil1'):
            qtd_perfil1 = detalhe_pop[1]
            for i in range(qtd_perfil1):
                populacao.append(gera_jogador(perfil1))
            total_pop -= qtd_perfil1

        if(detalhe_pop[0] == 'perfil2'):
            qtd_perfil2 = detalhe_pop[1]
            for i in range(qtd_perfil2):
                populacao.append(gera_jogador(perfil2))
            total_pop -= qtd_perfil2

        if(detalhe_pop[0] == 'perfil3'):
            qtd_perfil3 = detalhe_pop[1]
            for i in range(qtd_perfil3):
                populacao.append(gera_jogador(perfil3))
            total_pop -= qtd_perfil3

        if(detalhe_pop[0] == 'perfil4'):
            qtd_perfil4 = detalhe_pop[1]
            for i in range(qtd_perfil4):
                populacao.append(gera_jogador(perfil4))
            total_pop -= qtd_perfil4

    for i in range(total_pop):
        populacao.append(gera_jogador_aleatorio(lista_perfis))

    return populacao
