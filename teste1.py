import csv

nome = "Rodrigo"
erros = 0
ganhou = True
tema = "casa"
palavra = ""

dado1 = ["Rodrigo", "CASA", "CAMA", True, 2]
dado2 = ["Romario", "ESCRITORIO", "CANETA", True, 4]



with open("ranking/rank.csv", "a", newline='') as arq:
    campos = ['Nome', 'Tema', 'Palavra', 'Ganhou', 'Erros']
    # escritor = csv.DictWriter(arq, fieldnames=campos)
    # escritor.writeheader()
    caneta = csv.writer(arq)
    caneta.writerow(dado1)
    caneta.writerow(dado2)





# senha = "BISCOITO"
# gabarito = list(senha)
# mostrar = []
# alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZÇ"
# erro = 0


# for x in range(0, len(senha)):
#     mostrar.append("_")


# def verifica(palavra, escolha):
#     i = 0
#     for x in palavra:
#         if x == escolha:
#             mostrar[i] = x      
#         i = i + 1
        

# while True:
#     mostra2 = mostrar.copy()
    
#     for y in mostrar:
#         print(y, end=" ")

#     print(f"\n{senha}")

#     letra = input("Letra: ").upper()
#     verifica(senha, letra)
#     if mostra2 == mostrar:
#         erro = erro + 1
#     print(erro)
