import random as rd
import csv

casa = []
escola = []
restaurante = []
temas = ["casa","restaurante","escola"]

def txt_to_list(arquivo:str, lista):
    with open(arquivo, encoding="utf-8") as arq:
        linhas = arq.readlines()
        for linha in linhas:
            dado = linha.replace("\n", "")
            lista.append(dado)

txt_to_list("palavras/casa.txt", casa)
txt_to_list("palavras/escola.txt", escola)
txt_to_list("palavras/restaurante.txt", restaurante)

# palavra = rd.choice(casa)
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZÇ"

def print_erro(arquivo:str):
    img_erro = []
    with open(arquivo, encoding="utf-8") as arq:
        linhas = arq.readlines()
        for linha in linhas:
            dado = linha.replace("\n", "")
            img_erro.append(dado)

    for linha in img_erro:
        print(linha)
    
erro0 = "forca/0erro.txt"
erro1 = "forca/1erro.txt"
erro2 = "forca/2erro.txt"
erro3 = "forca/3erro.txt"
erro4 = "forca/4erro.txt"
erro5 = "forca/5erro.txt"
erro6 = "forca/6erro.txt"


def write_rank(dado):
    with open("ranking/rank.csv", "a", newline='') as arq:
        # campos = ['Nome', 'Tema', 'Palavra', 'Ganhou', 'Erros']
        caneta = csv.writer(arq)
        caneta.writerow(dado)



def novo_jogo():
    jogador = input("Digite seu nome: ").upper()

    tema = rd.choice(temas)
    senha = ""
    if tema == "casa":
        senha = rd.choice(casa)
    elif tema == "restaurante":
        senha = rd.choice(restaurante)
    elif tema == "escola":
        senha = rd.choice(escola)

    mostrar = []
    gabarito = list(senha)
    erro = 0

    for x in range(0, len(senha)):
        mostrar.append("_")

    def verifica(palavra, escolha):
        i = 0
        for x in palavra:
            if x == escolha:
                mostrar[i] = x
            i = i + 1

    while True:
        mostra2 = mostrar.copy()
        print(f"Tema: {tema.upper()}")


        if erro == 0:
            print_erro(erro0)
        elif erro == 1:
            print_erro(erro1)
        elif erro == 2:
            print_erro(erro2)
        elif erro == 3:
            print_erro(erro3)
        elif erro == 4:
            print_erro(erro4)
        elif erro == 5:
            print_erro(erro5)
        elif erro == 6:
            print_erro(erro6)


        for y in mostrar:
            print(y, end=" ")
        print(f"\n")

        if erro == 6:
            print(f"A palavra era: {senha}")
            dado = [jogador, tema, senha, False, erro]
            write_rank(dado)
            break

        letra = input("Digite uma letra: ").upper()
        verifica(senha, letra)

        if gabarito == mostrar:
            print(f"Parabéns {jogador}, você completou a palavra {senha}!")
            dado = [jogador, tema, senha, True, erro]
            write_rank(dado)
            break
        
        if mostra2 == mostrar:
            erro = erro + 1

def mostra_rankGeral():
    ranking = []
    qtd_ganhas = {}
    ganhadores = []
    ganhaOrdenados = []
    with open("ranking/rank.csv", encoding="utf-8") as rank:
        linhas = csv.DictReader(rank)
        for linha in linhas:
            ranking.append(linha)
    
    for partida in ranking:
        if partida["Ganhou"] == "True":
            ganhadores.append(partida["Nome"])
    
    
    for ganhador in ganhadores:
        if ganhador in qtd_ganhas:
            qtd_ganhas[ganhador] = qtd_ganhas.get(ganhador) + 1
        else:
            qtd_ganhas[ganhador] = 1
    
    for i in sorted(qtd_ganhas, key = qtd_ganhas.get, reverse=True):
        ganhaOrdenados.append({"Nome":i , "vitorias": qtd_ganhas[i]})

    y = 1
    print(f"N°. NOME{' '*10}VITÓRIAS")
    for x in ganhaOrdenados:
        print(f"{(y)} {x["Nome"]:20s}{x["vitorias"]}")
        y = y + 1

def rank_Jogador():
    ranking = []
    with open("ranking/rank.csv", encoding="utf-8") as rank:
        linhas = csv.DictReader(rank)
        for linha in linhas:
            ranking.append(linha)

    jogador = input("Nome do Jogador:").upper()
    print(f"{'NOME':20s} {'TEMA':10s} {'PALAVRA':10s} {'GANHOU':6s} {'ERROS'}")
    for partida in ranking:
        if partida["Nome"] == jogador:
            print(f"{partida['Nome']:20s} {partida['Tema']:10s} {partida['Palavra']:10s} {partida['Ganhou']:6s} {partida['Erros']}")

while True:
    print("1. Começar novo jogo")
    print("2. Ver ranking geral")
    print("3. Ver dados de um jogador")
    print("6. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        novo_jogo()
    elif opcao == 2:
        mostra_rankGeral()
    elif opcao == 3:
        rank_Jogador()
    else:
        break