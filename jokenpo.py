import random


def jogar():

    boasvindas()
    print(" ")
    total_de_tentativa = 5
    conta_empate, conta_acerto, conta_derrota = 0, 0, 0

    for rodada in range(1, total_de_tentativa + 1):

        usuario = input("Use 'r' para pedra, 'p' para papel e 's' para tesoura. "
                        "\nDigite sua tentativa aqui: ").lower().strip()
        comput = random.choice(["r", "p", "s"])

        print(f"Tentativa {rodada} de {total_de_tentativa}")

        acertou = usuario_venceu(usuario, comput)
        derrota = usuario_venceu(comput, usuario)
        empate = usuario == comput

        if empate:
            print(f"O computador jogou '{comput}'")
            print("")
            print('Empate.')
            print("")
            conta_empate += 1
            continue

        elif acertou:
            print(f"O computador jogou '{comput}'")
            print("")
            print('Você venceu!')
            print("")
            conta_acerto += 1
            continue

        elif derrota:
            print(f"O computador jogou '{comput}'")
            print("")
            print('Você perdeu! Tente novamente!')
            print("")
            conta_derrota += 1
            continue

        else:
            print("Digite apenas as letras válidas!\nLembre-se, use 'r' para pedra, 'p' para papel e 's' para tesoura.")
            break
    print(f"De {total_de_tentativa} tentativas, foram: "
          f"\n{conta_acerto} acertos \n{conta_derrota} derrotas \n{conta_empate} empates.")
    print("Fim de Jogo!")


def boasvindas():
    print("**************************************************")
    print(' Bem vindo(a) ao Jokenpô (Pedra, Papel, Tesoura)! ')
    print("**************************************************")


def usuario_venceu(jogador, oponente):
    if (jogador == "r" and oponente == "s") or (jogador == "s" and oponente == "p") or \
            (jogador == "p" and oponente == "r"):
        return True


if __name__ == "__main__":
    jogar()
