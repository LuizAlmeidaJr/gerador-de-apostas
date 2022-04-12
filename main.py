from time import sleep
from random import randint

dadosJogo = [{'nome': '\033[1;42mMEGA-SENA\033[m', 'num': 6, 'min': 1, 'max': 60, 'cor': 32},
            {'nome': '\033[1;46mLOTOFÁCIL\033[m', 'num': 15, 'min': 1, 'max': 25, 'cor': 36},
            {'nome': '\033[1;45mQUINA\033[m', 'num': 5, 'min': 1, 'max': 80, 'cor': 35},
            {'nome': '\033[1;43mLOTOMANIA\033[m', 'num': 50, 'min': 0, 'max': 99, 'cor': 33},
            {'nome': '\033[1;41mDUPLA-SENA\033[m', 'num': 6, 'min': 1, 'max': 50, 'cor': 31}]
aposta = []
dados = []


def escolheJogo():  # Verifica para qual jogo serão feitas as apostas
    while True:
        global jogo
        jogo = int(input('''Para qual jogo deseja fazer apostas?
        [1] {}
        [2] {}
        [3] {}
        [4] {}
        [5] {}

        Sua opção: '''.format(dadosJogo[0]['nome'], dadosJogo[1]['nome'], dadosJogo[2]['nome'], dadosJogo[3]['nome'], dadosJogo[4]['nome'])))
        print('')
        if 1 <= jogo <= 5:
            break
        else:
            print('Opção inválida. Tente novamente!')
            sleep(1)
            print('')


def numeroApostas (nomeJogo):  # Verifica o número de apostas a serem geradas para o jogo selecionado
    while True:
        global n
        n = int(input('Deseja gerar quantas apostas da {}? '.format(dadosJogo[nomeJogo - 1]['nome'])))
        if n > 0:
            break
        else:
            print('Valor inválido. Digite um valor maior que zero.')
            sleep(1)
            print('')


def geraApostas(nApostas, totNum, minNum, maxNum):  # Gera as apostas para o jogo selecionado
    global dados
    global aposta
    while len(dados) < nApostas:
        while len(aposta) < totNum:
            num = randint(minNum, maxNum)
            if num not in aposta:
                aposta.append(num)
        aposta.sort()
        if aposta not in dados:
            dados.append(aposta)
            del (aposta)
            aposta = []


def exibeApostas(nApostas, totNum):  # Exibe as apostas para o jogo selecionado
    if nApostas == 1:
        print('Gerando aposta...')
    else:
        print('Gerando apostas...')
    sleep(1)
    tam = 14 + 4 * dadosJogo[jogo - 1]['num']
    print(f"\033[{dadosJogo[jogo-1]['cor']}m*\033[m" * tam)
    print(f"APOSTAS {dadosJogo[jogo - 1]['nome']}")
    print('')
    for i in range(nApostas):
        dados[i].sort()
        if i < 9:
            print(f' {i + 1}ª aposta: [', end='')
        else:
            print(f'{i + 1}ª aposta: [', end='')
        for j in range(totNum - 1):
            print('{:>-3},'.format(dados[i][j]), end='')
        print('{:>-3}]'.format(dados[i][totNum - 1]))
        sleep(0.5)
    print('')
    print(f"\033[{dadosJogo[jogo-1]['cor']}m*\033[m" * tam)


def novaAposta():  # Gera novas apostas se o usuário desejar
    while True:
        print('')
        res = input('Deseja gerar novas apostas?[S/N] ').upper()[0]
        if res not in 'SN':
            print('Opção inválida!')
        elif res == 'N':
            print('')
            print('*' * 50)
            print('{:^50}'.format('BOA SORTE!!!'))
            print('*' * 50)
            break
        else:
            escolheJogo()
            numeroApostas(jogo)
            global dados
            dados = []
            geraApostas(n, dadosJogo[jogo - 1]['num'], dadosJogo[jogo - 1]['min'], dadosJogo[jogo - 1]['max'])
            exibeApostas(n, dadosJogo[jogo - 1]['num'])


#Programa principal
print('\033[32m$\033[m' * 15 + ' \033[32mLOTERIAS\033[m ' + '\033[32m$\033[m' * 15)
print('')
escolheJogo()
numeroApostas(jogo)
geraApostas(n, dadosJogo[jogo - 1]['num'], dadosJogo[jogo - 1]['min'], dadosJogo[jogo - 1]['max'])
exibeApostas(n, dadosJogo[jogo - 1]['num'])
novaAposta()
