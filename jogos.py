import adivinha
import forca
import jokenpo

def biblioteca_jogos():
    print("*************************************")
    print(' Bem vindo(a) a biblioteca de jogos! ')
    print("*************************************")

    print("Tenho 3 opções de jogos para você jogar: \n (1) Adivinha\n (2) Forca\n (3) Jokenpô")
    jogo = int(input("Digite o jogo que deseja jogar: "))

    print(" ")

    if jogo == 1:
        print("Iniciando o jogo de adivinha:")
        adivinha.jogar()
    elif jogo == 2:
        print("Iniciando o jogo da forca:")
        forca.jogar()
    elif jogo == 3:
        print("Iniciando o jokenpô:")
        jokenpo.jogar()
    else:
        print("Digite um número válido!")


if __name__ == "__main__":
    biblioteca_jogos()
