# coding=utf-8
import argparse

from jogo import jogadas
from populacao import gera_populacao
from populacao import evolui_pop


def main(args):
    populacao = gera_populacao(args.tiposPerfis, args.detalhesPop)
    for x in range(3):
        jogadas(populacao, x)
        evolui_pop(populacao, x)



def arg_parse():
    """ analisa e separa os argumentos passados ao iniciar a execucao """
    parser = argparse.ArgumentParser(description='new')
    parser.add_argument("--tiposPerfis", help="Tipos de perfis", default="tiposPerfis.txt")
    parser.add_argument("--detalhesPop", help="Detalhes da população a ser criada", default="detalhesPop.txt")

    return parser.parse_args()


if __name__ == '__main__':
    """ chama a func que analisa os argumentos e passa os argumentos para o main """
    arguments = arg_parse()
    main(arguments)
