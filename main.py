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
empates = 0
while modo == 1:
    print(f"\nMODO: Humano VS Humano selecionado")
    print(f"==OPÇÕES== \n1: 👊Pedra \n2: 🖐️Papel \n3: ✌️Tesoura")

    jogador1 = int(input("\nJogador 1: \n> "))
    while jogador1 != 1 and jogador1 != 2 and jogador1 != 3:
        jogador1 = input("\nJogador 1: \n> ")
    jogador2 = input("\nJogador 2: \n> ")
    while jogador2 != 1 and jogador2 != 2 and jogador2 != 3:
        jogador2 = input("\nJogador 2: \n> ")

    if jogador1 == jogador2:
        print("Empate!")
        empate += 1
    elif jogador1 == 1 and jogador2 == 2:
        print("Jogador 2 venceu!")
        ponto2 += 1
    elif jogador1 == 2 and jogador2 == 1:
        print("Jogador 1 venceu!")
        ponto1 += 1
    elif jogador1 == 3 and jogador2 == 2:
        print("Jogador 1 venceu!")
        ponto1 += 1
    elif jogador1 == 2 and jogador2 == 3:
        print("Jogador 2 venceu!")
        ponto2 += 1
    elif jogador1 == 3 and jogador2 == 1:
        print("Jogador 2 venceu!")
        ponto2 += 1
    elif jogador1 == 1 and jogador2 == 3:
        print("Jogador 1 venceu!")
        ponto1 += 1
    print(f"\n== PLACAR == \n  {ponto1} X {ponto2}")
    denovo = input("\nDeseja jogar novamente? [S/N] \n> ")
    if denovo.lower() == "n":
        print(f"\n=== PLACAR FINAL === \n JOGADOR 1 X JOGADOR 2 \n     {ponto1}     X     {ponto2}")
        print(f"\nEmpates: \n {empates}")
        print("\nObrigada por jogar! \nTrabalho feito por:\nPaola R. Leonardi\nHelena Gomes\nJuliana Munhoz")
        break
# --------------- Juliana: Computador x Humano ---
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

while modo == 2:
    print(f"\nMODO: Humano VS Computador selecionado")
    print(f"==OPÇÕES== \n1:👊Pedra \n2:🖐️Papel \n3:✌️Tesoura\n")
    usuario = int(input("Sua escolha:\n> "))

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

    print(f"\n == PLACAR == \n {pontuacao_usuario} x {pontuacao_computador}\n")
    novamente = str(input("Deseja jogar outra partida? [S/N] \n> ")).lower()
    if novamente.lower() == "n":
        print(f"\n=== PLACAR FINAL === \n USUÁRIO X COMPUTADOR \n    {pontuacao_usuario}    X     {pontuacao_computador}")
        print(f"\nEmpates: \n {empates}")
        print("\nObrigada por jogar! \nTrabalho feito por: \nHelena Gomes \nJuliana Munhoz \nPaola Leonardi")
        break
# --------------- Paola: Computador x Computador -
import random

pontos1 = 0
pontos2 = 0
empate = 0

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
            empate = empate +1

        elif (jogada1 == 1 and jogada2 == 3) or \
             (jogada1 == 3 and jogada2 == 2) or \
             (jogada1 == 2 and jogada2 == 1):
            print("Computador 1 venceu!")
            pontos1 += 1
        else:
            print("Computador 2 venceu!")
            pontos2 += 1

        print(f"\n== PLACAR == \n  {pontos1} X {pontos2}\n")
        denovo = str (input("Deseja jogar novamente? [S/N]\n> ").lower())

        if denovo.lower() == "n":
            print(f"\n=== PLACAR FINAL === \n  COMP 1 X COMP 2 \n     {pontos1}   X   {pontos2}")
            print(f"\nEmpates: \n {empate}")
            print ("\nObrigada por jogar! \nTrabalho feito por:\nPaola Leonardi\nHelena Gomes\nJuliana Munhoz")
            break
