import forca
import adivinhação

def escolhe_jogo():
    print('---------------------------------')
    print('BEM', 'VINDO', 'A', 'SALA', 'DE', 'JOGOS!', sep='-')
    print('---------------------------------')

    print('(1) Jogo da Forca (2) Jogo de Adivinhação ')

    jogo = int(input('SELECIONE O JOGO QUE DESEJA: '))

    if(jogo == 1):
        print('JOGO DA FORCA!')
        forca.jogar()
    elif(jogo == 2):
        print('JOGO DE ADIVINHAÇÃO!')
        adivinhação.jogar()   

# EXERCICIOS P/ PRATICAR NO LINK https://wiki.python.org.br/ListaDeExercicios


# EXEMPLOS DO WHILE (LOOP/REPETIÇÃO)
# total = 1
# palavra = "bianca"
# acabou = False
# while (not acabou):
#     acabou = (total == len(palavra))
#     print(acabou)
#     total = total + 1
# print(total - 1)

# passos = 0
# while (passos <=9):
#   passos += 1
# print(passos)