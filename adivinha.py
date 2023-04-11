import random

def jogar():
    print("************************************")
    print('Bem vindo(a) ao jogo de adivinhação!')
    print("************************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade deseja?\n (1) Fácil \n (2) Médio \n (3) Difícil")
    nivel = int(input("Digite o número da dificuldade: "))

    if nivel == 1:
        total_de_tentativas = 20

    elif nivel == 2:
        total_de_tentativas = 10

    elif nivel == 3:
        total_de_tentativas = 5

    else:
        print("Digite uma dificuldade válida!")

    for rodada in range(1, total_de_tentativas + 1):
        print(f'Tentativa {rodada} de {total_de_tentativas}')
        chute_str = input("Digite um número entre 1 e 100: ")
        print(f"Você digitou {chute_str}.")
        chute = int(chute_str)

        if chute < 0 or chute > 100:
            print("Digite um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print(f'Parabéns, você acertou! \nSua pontuação foi de {pontos} pontos!')
            break
        else:
            if maior:
                print("Você errou! O seu número foi maior que o número secreto.")
            elif menor:
                print("Você errou! O seu número foi menor que o número secreto.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    print("************************************")
    print("Fim do Jogo.")

if __name__ == "__main__":
    jogar()
