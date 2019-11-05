# coding=utf-8


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


def gera_populacao(txt):
    """ func geradora de população atraves de um txt"""
    massa_populacao = open(txt, "r")

    populacao = []

    if massa_populacao.mode == 'r':
        contents = massa_populacao.readlines()
        while contents:
            linha = contents.pop().replace("\n", "")
            atributos = linha.split(",")
            jogador = Jogador(
                perfil=atributos[0],
                conteudo_interesse=atributos[1],
                conteudo_publicado=atributos[2],
                qualidade_publicacao=atributos[3],
                frequencia_publicacao=atributos[4],
                minimo_consumo=atributos[5]
            )
            populacao.append(jogador)
    massa_populacao.close()

    return populacao
