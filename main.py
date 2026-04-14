# --------------- Menú ---------------------------
print ("JOKENPÔ")
print ("1: Humano VS Humano ")
print ("2: Computador VS Humano ")
print ("3: Computador VS Computador ")
print ("0: SAIR")
modo = int (input("Digite o número do modo que gostaria de jogar:\n> "))

# --------------- Helena: Humano x Humano --------

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

    denovo = str (input("Deseja jogar novamente? N/Y\n>").lower)
