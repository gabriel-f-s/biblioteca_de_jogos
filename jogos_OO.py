
class Jogos:

    @staticmethod
    def jogar_adivinha():
        print("Jogando Adivinha:")
        import adivinha
        adivinha.jogar()

    @staticmethod
    def jogar_forca():
        print("Jogando Forca:")
        import forca
        forca.jogar()

    @staticmethod
    def jogar_jokenpo():
        print("Jogando Jokenpô:")
        import jokenpo
        jokenpo.jogar()


class Jogar:
    print("*************************************")
    print(' Bem vindo(a) a biblioteca de jogos! ')
    print("*************************************")

    print("Tenho 3 opções de jogos para você jogar: \n (1) Adivinha\n (2) Forca\n (3) Jokenpô")
    jogo = int(input("Digite o jogo que deseja jogar: "))

    print(" ")

    if jogo == 1:
        print("Iniciando o jogo de adivinha:")
        Jogos.jogar_adivinha()

    elif jogo == 2:
        print("Iniciando o jogo da forca:")
        Jogos.jogar_forca()

    elif jogo == 3:
        print("Iniciando o jokenpô:")
        Jogos.jogar_jokenpo()

    else:
        print("Digite um número válido.")


print(Jogar)
