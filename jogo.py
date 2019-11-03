# coding=utf-8
from populacao import Player


def jogadas(jogadores: list):
    """ cada jogador deve jogar uma jogada individual com todos os outros jogadores da população.
        o resultado da jogada individual é a utilidade daquela interação, esse resultado deve ser armazenado e
        incrementado a cada iteração do jogador com outro membro da população.
    """
    for jogador_a in jogadores:
        print("\n\nPerfil jogador:", jogador_a.perfil)
        print("conteudo_interesse jogador:", jogador_a.conteudo_interesse)
        print("conteudo_publicado jogador:", jogador_a.conteudo_publicado)
        print("qualidade_publicacao jogador:", jogador_a.qualidade_publicacao)
        print("frequencia_publicacao jogador:", jogador_a.frequencia_publicacao)
        print("utilidade jogador:", jogador_a.utilidade)

        
        for jogador_b in jogadores:
            pass
        # fazer a jogada individual desse jogador com cada um um dos outros e armazenar o resultado de cada uma delas
        # fazer a media das utilidades de todas as jogads desse jogador
    pass


def jogada_individual(jogador: Player):
    pass


def utilidade_da_jogada():
    # calcular a media das utilidades
    pass

