# coding=utf-8
"""
V1 da Simulacao:
1- ter a definição os usuários que possuem perfis(com atributos de acordo com a equação de utilidade)
2- gerar uma populacao de usuários aleatoriamente (com tamanho y)
3- fazer a rodada de 1 user x todos os outros até que esse user tenha jogado com tds os outros
4- imprime resultados => valor da função de utilidade geral (somatório de todas as utlidades obtidas nas interações)
"""
from builtins import str


def generate_seed(desired_content, published_content, quality, frequency):
    seed = {}
    seed['desired_content'] = desired_content
    seed['published_content'] = published_content
    seed['quality'] = quality
    seed['frequency'] = frequency
    return seed


def generate_desired_content(desired_content_seed):
    return desired_content_seed


def generate_published_content(publish_content_seed):
    return publish_content_seed


def generate_quality(quality_seed):
    return quality_seed


def generate_frequency(frequency_seed):
    return frequency_seed



def get_profile_seed(argument):
    switcher = {
        "popular": generate_seed(['published','content'],['desired','content'],0.8,0.8),
        "shy": generate_seed(['published','content'],['desired','content'],0.2,0.1),
        "non_sense": generate_seed(['published','content'],['desired','content'],0.3,0.5)
    }
    return switcher.get(argument, "Invalid profile")


class Player:
    # TODO a frequencia e a qualidade ser especifica de cada tipo de conteudo (content) - sera que seria legal?
    def __init__(self, profile):

        profile_seed = get_profile_seed(profile)

        self.desired_content = generate_desired_content(profile_seed['desired_content'])
        self.published_content = generate_published_content(profile_seed['published_content'])
        self.quality = generate_quality(profile_seed['quality'])
        self.frequency = generate_frequency(profile_seed['frequency'])

    def __str__(self):
        string = "desired: "
        for i in self.desired_content:
            string += i
        string += " publish: "
        for x in self.published_content:
            string += x
        string += " quality: " + str(self.quality) + " frequency: " + str(self.frequency)
        return string


if __name__ == '__main__':
    player1 = Player('popular')
    player2 = Player('shy')
    player3 = Player('non_sense')
    print(player1)
    print(player2)
    print(player3)
