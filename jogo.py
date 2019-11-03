# coding=utf-8
from populacao import Player

def interesse(conteudo_interesse, conteudo_publicado):
    match = 0
    for conteudo in conteudo_interesse:
        if conteudo in conteudo_publicado:
            match = match + 1
    return match/len(conteudo_publicado)

def perda(frequencia, qualidade, interesse):
    return pow(frequencia,2)+pow((1-qualidade),2)+pow((1-interesse),2)

def ganho(frequencia, qualidade, interesse):
    return frequencia*qualidade*interesse

def consumo(frequencia, qualidade, interesse):
    return ganho(frequencia, qualidade, interesse) - perda(frequencia, qualidade, interesse)

def atencao(frequencia, qualidade, interesse):
    return frequencia*qualidade*interesse

def custo(frequencia, qualidade):
    return pow(frequencia*qualidade,2)

def jogada_individual(jogador_a: Player, jogador_b: Player):
    pass

def jogadas(jogadores: list):
    """ cada jogador deve jogar uma jogada individual com todos os outros jogadores da população.
        o resultado da jogada individual é a utilidade daquela interação, esse resultado deve ser armazenado e
        incrementado a cada iteração do jogador com outro membro da população.
    """
    for jogador_a in jogadores:
        #print("\n\nPerfil jogador:", jogador_a.perfil)
        #print("conteudo_interesse jogador:", jogador_a.conteudo_interesse)
        #print("conteudo_publicado jogador:", jogador_a.conteudo_publicado)
        #print("qualidade_publicacao jogador:", jogador_a.qualidade_publicacao)
        #print("frequencia_publicacao jogador:", jogador_a.frequencia_publicacao)
        #print("utilidade jogador:", jogador_a.utilidade)
        for jogador_b in jogadores:
            #jogada_individual(jogador_a,jogador_b)
            print("conteudo_interesse jogador A:", jogador_a.conteudo_interesse)
            print("conteudo_publicado jogador B:", jogador_b.conteudo_publicado)
            print("Frequencia jogador B:", jogador_b.frequencia_publicacao)
            print("Qualidade jogador B:", jogador_b.qualidade_publicacao)
            interesse_a_em_b = interesse(jogador_a.conteudo_interesse, jogador_b.conteudo_publicado)
            print("Interesse de A em B:", interesse_a_em_b)
            ganho_a_em_b = ganho(jogador_b.frequencia_publicacao, jogador_b.qualidade_publicacao, interesse_a_em_b)
            print("Ganho de A em B:", ganho_a_em_b)
            perda_a_em_b = perda(jogador_b.frequencia_publicacao, jogador_b.qualidade_publicacao, interesse_a_em_b)
            print("Perda de A em B:", perda_a_em_b)
            consumo_a_em_b = consumo(jogador_b.frequencia_publicacao, jogador_b.qualidade_publicacao, interesse_a_em_b)
            print("Consumo de A em B:", consumo_a_em_b)
            print("\n\n")
        # fazer a jogada individual desse jogador com cada um um dos outros e armazenar o resultado de cada uma delas
        # fazer a media das utilidades de todas as jogads desse jogador
