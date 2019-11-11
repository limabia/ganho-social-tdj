# coding=utf-8
import argparse

from jogo import jogadas
from populacao import gera_populacao


def main(args):
    # TODO implementar um gera populacao aleatoria utilizando o args.npop para definir o tamanho da pop
    populacao = gera_populacao(args.tiposPerfis, args.detalhesPop)
    print(populacao)
    jogadas(populacao)


def arg_parse():
    """ analisa e separa os argumentos passados ao iniciar a execucao """
    parser = argparse.ArgumentParser(description='new')
    parser.add_argument("--tiposPerfis", help="Tipos de perfis", default="")
    parser.add_argument("--detalhesPop", help="Detalhes da população a ser criada", default="")

    return parser.parse_args()


if __name__ == '__main__':
    """ chama a func que analisa os argumentos e passa os argumentos para o main """
    arguments = arg_parse()
    main(arguments)
