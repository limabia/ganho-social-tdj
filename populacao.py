# coding=utf-8


class Player:
    """ Classe que define o conjunto de argumentos que cada player tem"""

    def __init__(self, perfil, conteudo_interesse, conteudo_publicado, qualidade_publicacao, frequencia_publicacao):
        self.perfil = perfil
        self.conteudo_interesse = conteudo_interesse.split(";")
        self.conteudo_publicado = conteudo_publicado.split(";")
        self.qualidade_publicacao = qualidade_publicacao
        self.frequencia_publicacao = frequencia_publicacao
        self.utilidade = 0


def gera_populacao(txt):
    """ func geradora de população atraves de um txt"""
    massa_populacao = open(txt, "r")

    populacao = []

    if massa_populacao.mode == 'r':
        contents = massa_populacao.readlines()
        while contents:
            linha = contents.pop().replace("\n","")
            atributos = linha.split(",")
            player = Player(
                perfil=atributos[0],
                conteudo_interesse=atributos[1],
                conteudo_publicado=atributos[2],
                qualidade_publicacao=atributos[3],
                frequencia_publicacao=atributos[4]
            )
            populacao.append(player)
    massa_populacao.close()

    return populacao
