# coding=utf-8
import csv
arquivo_jogadas_ind = csv.writer(open("jogadas_individuais.csv", "w"))
arquivo_jogadas_ind.writerow([
    "jogador_a",
    "jogador_b",
    "interesses_JA",
    "publicado_JB",
    "frequencia_JB",
    "qualidade_JB",
    "interesse_JA_em_JB",
    "consumo_JA_em_JB",
    "minimo_consumo_JA",
    "JA_seguiu_JB",
    "JA_segue"
    ])
arquivo_jogadas = csv.writer(open("jogadas.csv", "w"))
arquivo_jogadas.writerow([
    "jogador",
    "utilidade"
    ])

jogador_a_seguiu_b: bool

def calcular_interesse(jogador_a, jogador_b):
    conteudo_interesse = jogador_a.conteudo_interesse
    conteudo_publicado = jogador_b.conteudo_publicado
    match = 0
    for conteudo in conteudo_interesse:
        if conteudo in conteudo_publicado:
            match = match + 1
    return match / len(conteudo_publicado)


def calcular_perda(jogador_a, jogador_b):
    return pow(jogador_b.frequencia_publicacao, 2) * pow((1 - jogador_b.qualidade_publicacao), 2) * pow(
        (1 - calcular_interesse(jogador_a, jogador_b)), 2)


def calcular_ganho(jogador_a, jogador_b):
    return jogador_b.frequencia_publicacao * jogador_b.qualidade_publicacao * calcular_interesse(jogador_a, jogador_b)


def calcular_consumo(jogador_a, jogador_b):
    return calcular_ganho(jogador_a, jogador_b) - calcular_perda(jogador_a, jogador_b)


def calcular_atencao(jogador_a, jogador_b):
    return jogador_a.frequencia_publicacao * jogador_a.qualidade_publicacao * calcular_interesse(jogador_b, jogador_a)


def calcular_custo(jogador):
    return pow(jogador.frequencia_publicacao * jogador.qualidade_publicacao, 2)


def jogada_individual(jogador_a, jogador_b):
    print("jogador A:", jogador_a.perfil, " Jogador B: ", jogador_b.perfil)
    print("conteudo_interesse jogador A:", jogador_a.conteudo_interesse)
    print("conteudo_publicado jogador B:", jogador_b.conteudo_publicado)
    print("Frequencia jogador B:", jogador_b.frequencia_publicacao)
    print("Qualidade jogador B:", jogador_b.qualidade_publicacao)
    interesse_a_em_b = calcular_interesse(jogador_a, jogador_b)
    print("Interesse de A em B:", interesse_a_em_b)
    consumo_a_em_b = 0.0
    jogador_a_seguiu_b = 0;
    if interesse_a_em_b != 0:
        consumo_a_em_b = calcular_consumo(jogador_a, jogador_b)
        print("Consumo de A em B:", consumo_a_em_b)
        print("Minimo para jogador A seguir B: ", jogador_a.minimoConsumo)
        if consumo_a_em_b >= jogador_a.minimoConsumo:
            print("Jogador A seguiu B")
            jogador_a_seguiu_b = 1
            jogador_b.seguidores.append(jogador_a)
            jogador_a.segue.append(jogador_b)
        else:
            print("Jogador A não seguiu B")
            jogador_a_seguiu_b = 0
    else:
        print("Jogador A não seguiu B")
    print("\n\n")
    arquivo_jogadas_ind.writerow([
        str(jogador_a.perfil),
        str(jogador_b.perfil),
        str(jogador_a.conteudo_interesse),
        str(jogador_b.conteudo_publicado),
        str(jogador_b.frequencia_publicacao),
        str(jogador_b.qualidade_publicacao),
        str(interesse_a_em_b),
        str(consumo_a_em_b),
        str(jogador_a.minimoConsumo),
        str(jogador_a_seguiu_b),
        str(jogador_a.segue)
        ])    


def calcular_utilidade(jogador_a):
    consumo = 0.0
    atencao = 0.0
    for jogador_seguido_por_a in jogador_a.segue:
        consumo += calcular_consumo(jogador_a, jogador_seguido_por_a)
    for jogador_que_segue_a in jogador_a.seguidores:
        atencao += calcular_atencao(jogador_a, jogador_que_segue_a)
    custo = calcular_custo(jogador_a)
    return consumo + atencao + custo


def jogadas(jogadores: list):
    """ cada jogador deve jogar uma jogada individual com todos os outros jogadores da população.
        o resultado da jogada individual é a utilidade daquela interação, esse resultado deve ser armazenado e
        incrementado a cada iteração do jogador com outro membro da população.
    """
    i = 0
    for jogador_a in jogadores:
        adversarios = jogadores.copy()
        adversarios.remove(jogador_a)
        for jogador_b in adversarios:
            print('jogador a: ', jogador_a, 'jogador b: ', jogador_b)
            jogada_individual(jogador_a, jogador_b)
            i += 1

    for jogador in jogadores:
        print("\n")
        print("Jogador:", jogador.perfil)
        jogador.utilidade = calcular_utilidade(jogador)
        print("Utilidade:", jogador.utilidade)
        arquivo_jogadas.writerow([
            str(jogador.perfil),
            str(jogador.utilidade)
        ])
