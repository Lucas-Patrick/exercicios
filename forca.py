import random

def jogar():
    imprime_mensagem_abetura() #1
    palavra_secreta =  carrega_palavra_secreta() #2

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)#3
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
    #while serve para fazer um loop

        chute = pede_chute()
        print('')

        if(chute in palavra_secreta): #4
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        
        print(letras_acertadas)
        

    if(acertou): #5
        imprime_mensagem_vencedor()
    else:
        mensagem_enforcou(palavra_secreta) #6

def desenha_forca(erros):
    print("          ___     ")
    print("     |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print("     |            ")
    print("     |__         ")
    print()
    

# ____________________________REPARTIÇÃO_DE_FUNCÕES_____________________________________

def imprime_mensagem_abetura(): #1
    print('#####################')
    print('JOGO', 'DA', 'FORCA!', sep='-')
    print('#####################')

def carrega_palavra_secreta(): #2
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta): #3
    return ["_" for letra in palavra_secreta]


def pede_chute(): #4
    chute = input("Selecione uma letra:  ")
    chute = chute.strip().upper() #.strip() e uma buit-in para eliminar o espaço da entrada do chute/e tirar o \n - pular linha em codigo
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
            letras_faltando = (letras_acertadas.count('_'))
        index += 1

    print('Ainda faltam acertar {} letras'.format(letras_faltando))

def imprime_mensagem_vencedor(): #5
    print('VOCÊ SE LIVROU, PARABENS!', 'YOU WIN',sep='---')
    print("       ___________      ")
    print("      '.=====.===='     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.      |) |    ")
    print("      '-|:.      |-'     ")
    print("        \\::.    /      ")
    print("         '::.  .'        ")
    print("           )   (          ")
    print("         _.'    '._        ")
    print("        '------+=-'       ")
    

def mensagem_enforcou(palavra_secreta): #6
    print('VOCÊ','SE', 'ENFORCOU!', 'GAME OVER!', sep='-')
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________   ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_          _/         ")
    print("       \___/\___/           ")


print('FIM', 'DE', 'JOGO!', sep='-------')

if(__name__ == '__main__'):#para rodar como programa principal 
    jogar()

# exemplo do FOR como ele funciona:
# palavra = "Alura"
# for letra in palavra:
#     print(letra)
#     if(letra == "l"):
#         print("Achou!")

# EXEMPLO DA LISTA
# frutas = ['Banana', 'Maca', 'Pera', 'Uva', 'Melancia', 'Jamelão']

# fruta_pedida = input('Qual é a fruta que deseja consultar ? :') 
# fruta_pedida = fruta_pedida.strip()

# if(fruta_pedida.capitalize() in frutas): 
#     #capitaize() serve para formular o que for escrito se for maiusculo/minusculo
#     print ('Sim, temos a fruta.')
# else:
#     print ('Não temos a fruta.')

# EXEMPLO P/ ACHAR O MENOR VALOR NA LISTA USANDO O (min)
# precos = [1525,1120,1464,1200,1330,1356,1312,1531,1232, 1234,1250,1114,1553,1147,1303,1296,1309,1404,1479,1376,1152,1440,1038,1018,1291,1388,1577,1115,1488,1494,1254,1230,1122,1396,1208,1356,1549,1116,1443,1075,1536,1542,1036,1015,1020,1217,1484,1032,1390,1026 ]
# print(min(precos))
# para saber o menor valor foi utilizado o print(min(variavel)) para saber o menor valor da lista

# EXEMPLO DA BUINT-IN len() QUE E USADA CONTAR QUANTOS ITENS TEM NA LISTA 
# funcionarios = ['lucas', 'bianca', 'isaac', 'ana']
# print(len(funcionarios)) 

# EXEMPLO DE LER AS LINHAS
#  arquivo = open('pessoas.txt', 'r')
# linha = arquivo.readline() - READLINE() PARA MOSTRA LINHA POR LINHA 
# print(linha)

