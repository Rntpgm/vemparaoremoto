
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


#Meu Codigo le um nome e o Usuario tem que 'acerta o nome' se nao ele nao entra no sistema
#ele entra no loop se for acertivo ele entra no sistema e sai do loop