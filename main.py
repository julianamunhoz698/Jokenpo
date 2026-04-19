# --------------- Menú ---------------------------
print ("JOKENPÔ")
print ("1: Humano VS Humano ")
print ("2: Computador VS Humano ")
print ("3: Computador VS Computador ")
print ("0: SAIR")
modo = int (input("Digite o número do modo que gostaria de jogar:\n> "))

# --------------- Helena: Humano x Humano --------
ponto1 = 0
ponto2 = 0
while modo == 1:
    print(f"\nMODO: Humano VS Humano")
    print(f"==OPÇÕES== \n👊Pedra \n🖐️Papel \n✌️Tesoura")

    jogador1 = str(input("\nJogador 1: \n> "))
    while jogador1.lower() != "pedra" and jogador1.lower() != "papel" and jogador1.lower() != "tesoura":
        jogador1 = str(input("J\nogador 1: \n> "))
    jogador2 = str(input("\nJogador 2: \n> "))
    while jogador2.lower() != "pedra" and jogador2.lower() != "papel" and jogador2.lower() != "tesoura":
        jogador2 = str(input("\nJogador 2: \n> "))

    if jogador1.lower() == jogador2.lower():
        print("Empate!")
    elif jogador1.lower() == "pedra" and jogador2.lower() == "papel":
        print("Jogador 2 venceu!")
        ponto2 += 1
    elif jogador1.lower() == "papel" and jogador2.lower() == "pedra":
        print("Jogador 1 venceu!")
        ponto1 += 1
    elif jogador1.lower() == "tesoura" and jogador2.lower() == "papel":
        print("Jogador 1 venceu!")
        ponto1 += 1
    elif jogador1.lower() == "papel" and jogador2.lower() == "tesoura":
        print("Jogador 2 venceu!")
        ponto2 += 1
    elif jogador1.lower() == "tesoura" and jogador2.lower() == "pedra":
        print("Jogador 2 venceu!")
        ponto2 += 1
    elif jogador1.lower() == "pedra" and jogador2.lower() == "tesoura":
        print("Jogador 1 venceu!")
        ponto1 += 1
    print(f"\n==PLACAR== \n  {ponto1} X {ponto2}")
    denovo = input("\nDeseja jogar novamente? [S/N] \n> ")
    if denovo.lower() == "n":
        print(f"\n=== RESULTADO FINAL === \n JOGADOR 1 X JOGADOR 2 \n     {ponto1}     X     {ponto2}")
        print("\nObrigada por jogar! \nAlunas responsáveis:\nPaola R. Leonardi\nHelena Gomes\nJuliana Munhoz")
        break
# --------------- Juliana: Computador x Humano ---
#Humano x Computador - Juliana


import random

#Variáveis
pontuacao_usuario = 0
pontuacao_computador = 0
vitorias = 0
derrotas = 0
empates = 0
partidas = 0
pedra = 1
papel = 2
tesoura = 3

while True:
    print ("Escolha uma das três opções: pedra(1), papel(2) ou tesoura(3)")
    usuario = int(input("Sua escolha: "))

    computador = random.randint(1, 3)
    print(f"O computador jogou: {computador}")

    partidas +=1

    if usuario == computador:
        print("Empate!")
        empates +=1
        pontuacao_usuario +=1
        pontuacao_computador +=1
    elif computador == 1:
        if usuario == 2:
            print("Você venceu!")
            vitorias +=1
            pontuacao_usuario +=1
        elif usuario == 3:
            print("Você perdeu!")
            derrotas +=1
            pontuacao_computador +=1
        else:
            print("Jogada inválida!")
    elif computador == 2:
        if usuario == 1:
            print("Você perdeu!")
            derrotas +=1
            pontuacao_computador +=1
        elif usuario == 3:
            print("Você venceu!")
            vitorias +=1
            pontuacao_usuario +=1
        else:
            print("Jogada inválida!")
    elif computador == 3:
        if usuario == 1:
            print("Você venceu!")
            vitorias +=1
            pontuacao_usuario +=1
        elif usuario == 2:
            print("Você perdeu!")
            derrotas +=1
            pontuacao_computador +=1
        else:
            print("Jogada inválida!")

    print (f"\n === Placar === \n Usuário x Computador \n {pontuacao_usuario} x {pontuacao_computador}")
    print (f"\nVitórias: \n {vitorias}")
    print (f"\nEmpates: \n {empates}")
    print (f"\nderrotas: \n {derrotas}")
    novamente = str(input("Deseja jogar outra partida? [sim/não] \n> ")).lower()
    if novamente.lower() == "não":
        print(f"\n=== Placar Final === \n Usuário x Computador \n {pontuacao_usuario} x {pontuacao_computador}")
        print(f"\nVitórias: \n {vitorias}")
        print(f"\nEmpates: \n {empates}")
        print(f"\nderrotas: \n {derrotas}")
        print (f"\npartidas: \n {partidas}")
        print("\nObrigada por jogar! \n Trabalho feito por: \n Helena Gomes\n Juliana Munhoz\n Paola Leonardi")
        break
# --------------- Paola: Computador x Computador -
import random

pontos1 = 0
pontos2 = 0

if modo == 3:
    print("MODO: Computador VS Computador selecionado")
    print(f"==OPÇÕES== \n👊Pedra \n🖐️Papel \n✌️Tesoura\n")

    while True:
        jogada1 = random.randint(1, 3)
        jogada2 = random.randint(1, 3)

        if jogada1 == 1:
            print("Jogador 1: Pedra")
        elif jogada1 == 2:
            print("Jogador 1: Papel")
        else:
            print("Jogador 1: Tesoura")

        if jogada2 == 1:
            print("Jogador 2: Pedra")
        elif jogada2 == 2:
            print("Jogador 2: Papel")
        else:
            print("Jogador 2: Tesoura")

        if jogada1 == jogada2:
            print("Empate!")

        elif (jogada1 == 1 and jogada2 == 3) or \
             (jogada1 == 3 and jogada2 == 2) or \
             (jogada1 == 2 and jogada2 == 1):
            print("Jogador 1 venceu!")
            pontos1 += 1
        else:
            print("Jogador 2 venceu!")
            pontos2 += 1
        print(f"Placar atual: {pontos1} x {pontos2}\n")
        denovo = str (input("Deseja jogar novamente? N/Y\n>").lower())

        if denovo.lower() == "n":

            print("\n=== RESULTADO FINAL ===")
            print(f"Jogador 1: {pontos1}")
            print(f"Jogador 2: {pontos2}")

            print ("\nObrigada por jogar!\n")
            print ("Alunas responsáveis:\nPaola R. Leonardi\nHelena Gomes\nJuliana Munhoz")
            break
