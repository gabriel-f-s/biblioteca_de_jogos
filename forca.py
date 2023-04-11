import random

 # Função principal:
def jogar():

    boasvindas()
    palavra_secreta = carregamento_palavra_secreta()
    letras_acertadas = init_acertos(palavra_secreta)

    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 0

    while not enforcou and not acertou:
        chute = funcao_chute()

        if chute in palavra_secreta:
            marcador_pts_correto(chute, letras_acertadas, palavra_secreta)

        else:
            tentativas += 1
            desenha_forca(tentativas)
            print(f"Tentativa {tentativas} de 7")

        enforcou = tentativas == 7
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        mensagem_vitoria()
    else:
        mensagem_derrota(palavra_secreta)

    print("************************************")
    print("Fim do Jogo.")


 # Funções complementares:
def boasvindas():
    print("************************************")
    print('   Bem vindo(a) ao jogo da forca!   ')
    print("************************************")

def carregamento_palavra_secreta():
    arquivo = open("frutas.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def init_acertos(palavra):
    return ["_" for letra in palavra]

def funcao_chute():
    chute = input("Digite a letra: ")
    chute = chute.strip().upper()
    return chute

def marcador_pts_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute.upper() == letra.upper():
            letras_acertadas[index] = letra
        index += 1

def mensagem_vitoria():
    print("Parabéns! Você ganhou!\nAqui está o seu troféu: 🏆")

def mensagem_derrota(palavra_secreta):
    print(f"Você errou! Tente novamente!\nA palavra era {palavra_secreta.lower()}.")
    print('███████████████████████████')
    print('███████▀▀▀░░░░░░░▀▀▀███████')
    print('████▀░░░░░░░░░░░░░░░░░▀████')
    print('███│░░░░░░░░░░░░░░░░░░░│███')
    print('██▌│░░░░░░░░░░░░░░░░░░░│▐██')
    print('██░└┐░░░░░░░░░░░░░░░░░┌┘░██')
    print('██░░└┐░░░░░░░░░░░░░░░┌┘░░██')
    print('██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██')
    print('██▌░│██████▌░░░▐██████│░▐██')
    print('███░│▐███▀▀░░▄░░▀▀███▌│░███')
    print('██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██')
    print('██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██')
    print('████▄─┘██▌░░░░░░░▐██└─▄████')
    print('█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████')
    print('████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████')
    print('█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████')
    print('███████▄░░░░░░░░░░░▄███████')
    print('██████████▄▄▄▄▄▄▄██████████')
    print('███████████████████████████')

def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == "__main__":
    jogar()