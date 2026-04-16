# --------------- Menú ---------------------------
print ("JOKENPÔ")
print ("1: Humano VS Humano ")
print ("2: Computador VS Humano ")
print ("3: Computador VS Computador ")
print ("0: SAIR")
modo = int (input("Digite o número do modo que gostaria de jogar:\n> "))
#-
# --------------- Helena: Humano x Humano --------
ponto1 = 0
ponto2 = 0
while modo == 1:
    print(f"Modo selecionado: Humano VS Humano")
    print(f"Opções: \nPedra \nPapel \nTesoura")

    jogador1 = str(input("Jogador 1: \n> "))
    while jogador1.lower() != "pedra" and jogador1.lower() != "papel" and jogador1.lower() != "tesoura":
        jogador1 = str(input("Jogador 1: \n> "))
    jogador2 = str(input("Jogador 2: \n> "))
    while jogador2.lower() != "pedra" and jogador2.lower() != "papel" and jogador2.lower() != "tesoura":
        jogador2 = str(input("Jogador 2: \n> "))

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
    print(f"\nPontuação: {ponto1} X {ponto2}")
    denovo = input("\nDeseja jogar novamente? [S/N] \n> ")
    if denovo.lower() == "n":
        print("Obrigada por jogar!")
        break
# --------------- Juliana: Computador x Humano ---

# --------------- Paola: Computador x Computador -
import random
if modo == 3:
    print ("MODO: Computador VS Computador selecionado")
    jogada1 = random.randint(1, 3)
    jogada2 = random.randint(1, 3)

while True:
    if jogada1 == 1:
        print (f"pedra")
    elif jogada1 == 2:
        print (f"papel")
    elif jogada1 == 3:
        print(f"tesoura")

    if jogada2 == 1:
        print (f"pedra")
    elif jogada2 == 2:
        print (f"papel")
    elif jogada2 == 3:
        print(f"tesoura")
    if jogada1 == jogada2:
        print ("Empate!")
    else:
        print ("Não houve empate!")

    denovo = str (input("Deseja jogar novamente? N/Y\n>").lower())

    if denovo != "Y":
        break
