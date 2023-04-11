import random

def jogar():

    boasvindas()
    usuario = input("Use 'r' para pedra, 'p' para papel e 's' para tesoura. \nDigite sua tentativa aqui: ").lower().strip()
    comput = random.choice(["r", "p", "s"])

    acertou = usuario_venceu(usuario, comput)
    derrota = usuario_venceu(comput, usuario)
    empate = usuario == comput

    print(" ")

    if empate:
        print(f"O computador jogou '{comput}'")
        print('Empate.')

    elif acertou:
        print(f"O computador jogou '{comput}'")
        print('Você venceu!')

    elif derrota:
        print(f"O computador jogou '{comput}'")
        print('Você perdeu! Tente novamente!')

    else:
        print("Digite apenas as letras válidas!\nLembre-se, use 'r' para pedra, 'p' para papel e 's' para tesoura.")

    print(" ")

    tentativa = input("Deseja tentar novamente?\nDigite 's' para sim e 'n' para não: ")
    if tentativa == 's':
        print(" ")
        jogar_novamente(empate, acertou, derrota)

    elif tentativa == 'n':
        print("************************************")
        print("Fim do Jogo.")

    else:
        print("Digite apenas 's' ou 'n'.")
        print("***************************************")
        print("Fim do Jogo.")


def boasvindas():
    print("**************************************************")
    print(' Bem vindo(a) ao Jokenpô (Pedra, Papel, Tesoura)! ')
    print("**************************************************")

def usuario_venceu(jogador, oponente):
    if (jogador == "r" and oponente == "s") or (jogador == "s" and oponente == "p") or \
            (jogador == "p" and oponente == "r"):
        return True

def jogar_novamente(empate, acertou, derrota):
    usuario = input(
        "Use 'r' para pedra, 'p' para papel e 's' para tesoura. \nDigite sua tentativa aqui: ").lower().strip()
    comput = random.choice(["r", "p", "s"])

    acertou = usuario_venceu(usuario, comput)
    derrota = usuario_venceu(comput, usuario)
    empate = usuario == comput

    print(" ")
    if empate:
        print(f"O computador jogou '{comput}'")
        print('Empate.')

    elif acertou:
        print(f"O computador jogou '{comput}'")
        print('Você venceu!')

    elif derrota:
        print(f"O computador jogou '{comput}'")
        print('Você perdeu! Tente novamente!')

    else:
        print("Digite apenas as letras válidas!\nLembre-se, use 'r' para pedra, 'p' para papel e 's' para tesoura.")

    print(" ")

    tentativa = input("Deseja tentar novamente?\nDigite 's' para sim e 'n' para não: ")
    if tentativa == 's':
        print(" ")
        jogar_novamente(empate, acertou, derrota)

    elif tentativa == 'n':
        print("************************************")
        print("Fim do Jogo.")

if __name__ == "__main__":
    jogar()