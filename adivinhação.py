import random # biblioteca feita para fazer ou criar um numero aleatorio
from tkinter import N

def jogar(): #def - para definir uma função

    imprime_msg_abertura()
    numero_secreto, pontos = guarda_numero_secreto()
    
    escolha_nivel()

    nivel = int(input('ESCOLHA A DIFICULDADE DO JOGO: '))

    if(nivel == 1):
        total_de_tentativas = 10
    elif(nivel == 2):
        total_de_tentativas = 5
    else:
        total_de_tentativas = 3

    # while = recebe uma condição de entrada
    for rodada in range(1, total_de_tentativas + 1):
        print('Tentativa {} de {}'.format(rodada,  total_de_tentativas))
        # input = para informar um numero com frase 
        # criar uma variavel usando o input 
        chute = int(input('DIGITE UM NÚMERO ENTRE 1 À 50: '))

        if (chute < 1 or chute > 50):
            print('VOCÊ DEVE DIGITAR UM NÚMERO DE 1 À 50')
            continue

        acerto, maior, menor = igualdade_acertos(numero_secreto, chute)

        print('VOCÊ DIGITOU O NUMERO:' , chute)

        if (acerto):
            print('PARABÉN! VOCÊ ACERTOU O NÚMERO SECRETO E FEZ {} PONTOS'.format(pontos)) # {}.format serve para informar a variavel que queremos com algo equivalente (intapulação) 
            break
        else:
            if(maior):
                print("O SEU CHUTE FOI MAIOR DO QUE O NÚMERO SECRETO!")
            elif(menor):
                print('O SEU CHUTE FOI MENOR QUE O NÚMERO SECRETO!')
            prontos_perdidos = abs(numero_secreto - chute) #abs() - serve para deixar um numero absoluto
            pontos = prontos_perdidos - chute
            
    print('FIM', 'DE', 'JOGO!', sep='-------')
    print('O NÚMERO SECRETO ERA: ', numero_secreto, sep='--> ')

def igualdade_acertos(numero_secreto, chute):
    acerto = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    return acerto,maior,menor

def escolha_nivel():
    print('ESCOLHA O NÍVEL DO JOGO! ')
    print('(1) Fácil (2) Médio (3) Difícil')

def guarda_numero_secreto():
    numero_secreto = random.randrange(1, 51) # blibloteca random, feita para deixar o numero inteiro
    total_de_tentativas = 0
    pontos = 1000
    return numero_secreto,pontos

def imprime_msg_abertura():
    print('#####################')
    print('--BEM', 'JOGO', 'DE', 'ADIVINHAÇÃO--', sep='--')
    print('#####################')

if(__name__== '__main__'):
    jogar()
    



# print('data do aniversario da bia é:{:02d}/{:02d}/{:02d}'.format(27,5,1999)) EXEMPLO DO .FORMAT (intepulaçao)

# import random

# sorteado = random.randrange(0,3)

# print(sorteado)

# if sorteado == 1:
#     print( "Paulo")
# elif sorteado == 2:
#     print("Juliana")
# else:
#     print("Tamires")