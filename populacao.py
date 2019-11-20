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

    def __init__(self, perfil, conteudo_interesse, conteudo_publicado, qualidade_publicacao, frequencia_publicacao,
                 minimo_consumo):
        self.perfil = perfil
        self.conteudo_interesse = conteudo_interesse
        self.conteudo_publicado = conteudo_publicado
        self.qualidade_publicacao = float(qualidade_publicacao)
        self.frequencia_publicacao = float(frequencia_publicacao)
        self.minimoConsumo = float(minimo_consumo)
        self.segue = []
        self.seguidores = []

    def __repr__(self):
        return self.perfil

    def __str__(self):
        return self.perfil


def gera_qualidade(faixa_qualidade):
    if faixa_qualidade == 'alta':
        return random.uniform(0.7, 0.99)
    if faixa_qualidade == 'media':
        return random.uniform(0.3, 0.7)
    if faixa_qualidade == 'baixa':
        return random.uniform(0, 0.3)


def gera_frequencia(faixa_frequencia):
    if faixa_frequencia == 'alta':
        return random.uniform(0.7, 0.99)
    if faixa_frequencia == 'media':
        return random.uniform(0.3, 0.7)
    if faixa_frequencia == 'baixa':
        return random.uniform(0, 0.3)


def gera_faixa_conteudo(conteudo_aleatorio, i, tipos_conteudo):
    for x in range(i):
        random_index = randint(0, len(tipos_conteudo) - 1)
        while tipos_conteudo[random_index] in conteudo_aleatorio:
            random_index = randint(0, len(tipos_conteudo) - 1)
        conteudo_aleatorio.append(tipos_conteudo[random_index])
    return conteudo_aleatorio


def gera_conteudo(faixa_conteudo):
    tipos_conteudo = ['comida', 'meme', 'atividades', 'selfies', 'fotos_em_grupo']
    conteudo_aleatorio = []

    if faixa_conteudo == 'alta':
        return tipos_conteudo

    if faixa_conteudo == 'media':
        i = randint(3, 4)
        return gera_faixa_conteudo(conteudo_aleatorio, i, tipos_conteudo)

    if faixa_conteudo == 'baixa':
        i = randint(1, 2)
        return gera_faixa_conteudo(conteudo_aleatorio, i, tipos_conteudo)


def gera_limiar(faixa_limiar):
    if faixa_limiar == 'alto':
        return random.uniform(0.5, 1)
    if faixa_limiar == 'medio':
        return random.uniform(0, 0.5)
    if faixa_limiar == 'baixo':
        return 0


def gera_jogador(atributos, nome_perfil):
    interesse = gera_conteudo(atributos[1])
    publicado = gera_conteudo(atributos[2])
    qualidade = gera_qualidade(atributos[3])
    frequencia = gera_frequencia(atributos[4])
    limiar = gera_limiar(atributos[5])

    jogador = Jogador(
        perfil=nome_perfil,
        conteudo_interesse=interesse,
        conteudo_publicado=publicado,
        qualidade_publicacao=qualidade,
        frequencia_publicacao=frequencia,
        minimo_consumo=limiar
    )
    return jogador


def gera_getalhes(pathFile):
    file_open = open(pathFile, "r")
    lista = []
    if file_open.mode == 'r':
        contents = file_open.readlines()
        while contents:
            linha = contents.pop().replace("\n", "")
            atributos = linha.split(",")
            lista.append(atributos)
    file_open.close()
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
        if detalhe_pop[0] == 'pop':
            total_pop = int(detalhe_pop[1])

        if detalhe_pop[0] in perfil_dict:
            qtd_perfil1 = int(detalhe_pop[1])
            for i in range(qtd_perfil1):
                nome_perfil = perfil_dict[detalhe_pop[0]][0] + '-' + str(i)
                populacao.append(gera_jogador(perfil_dict[detalhe_pop[0]], nome_perfil))
            total_pop -= qtd_perfil1

    return populacao
