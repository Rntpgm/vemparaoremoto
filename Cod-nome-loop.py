
contador = 0
while True:
    nome = input("qual e seu nome? ")

    if nome == "Renato":
        print("Sim! este e o nome certo")
        break
    else:
        contador += 1  # Incrementa o contador
        print("Digite novamente")
print(f"Voce digitou {contador} vezes.")


