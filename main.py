# --------------- Menú ---------------------------
print ("JOKENPÔ")
print ("1: Humano VS Humano ")
print ("2: Computador VS Humano ")
print ("3: Computador VS Computador ")
print ("0: SAIR")
modo = int (input("Digite o número do modo que gostaria de jogar:\n> "))
#-
# --------------- Helena: Humano x Humano --------

# --------------- Juliana: Computador x Humano ---

# --------------- Paola: Computador x Computador -
import random #Importada uma biblioteca p fzer números aleatórios

pontos1 = 0
pontos2 = 0

if modo == 3:
    print("MODO: Computador VS ComputADOR selecionado")

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

        elif (jogada1 == 1 and jogada2 == 3) or \ #o "\" diz q essa linha ainda não acabou, continua na próxima
             (jogada1 == 3 and jogada2 == 2) or \
             (jogada1 == 2 and jogada2 == 1):
            print("Jogador 1 venceu!")
            pontos1 += 1
        else:
            print("Jogador 2 venceu!")
            pontos2 += 1
        print(f"Placar final: {pontos1} x {pontos2}")
        denovo = str (input("Deseja jogar novamente? N/Y\n>").lower())

        if denovo != "y":
            break

    print("\n RESULTADO FINAL ")
    print(f"Jogador 1: {pontos1}")
    print(f"Jogador 2: {pontos2}")
