from menus import *
from registro import *
from funcoes import *

regPro = []
regCor = []
regCli = []
regImo = []

for i in range (1):
    regImo.append(IMOVEL())
    regImo[0].codigoImovel = 1
    regImo[0].tipo = 'Venda'
    regImo[0].rua = 'Europa'
    regImo[0].setor = 'Área Alfa'
    regImo[0].NCasa = 'sn'
    regImo[0].tamanho = 1000
    regImo[0].quarto = 2
    regImo[0].tamanhoQuarto.append(40)
    regImo[0].tamanhoQuarto.append(40)
    regImo[0].banheiro = 1
    regImo[0].tamanhoBanheiro.append(20)
    regImo[0].status = 'À Venda'
for i in range (1):
    regPro.append(PROPRIETARIO())
    regPro[i].cod = '2909'
    regPro[i].nome = 'Gustavo Xavier Pericole'
    regPro[i].cpf = '04569258131'
    regPro[i].rg = '123456789'
    regPro[i].imovelPossuido.append(1)

for i in range (1):
    regCor.append(CORRETOR())
    regCor[i].cod = '6969'
    regCor[i].nome = 'Jorge Lucas Da Silva'
    regCor[i].cpf = '12345678909'
    regCor[i].rg = '987654321'

sair = False
while True:

    escolhaInicial =  menuInicial () #função do menu inicial

    while True:
        if escolhaInicial == 0: #condicional que avalia o resultado da função (menuInicial) caso vale 0(Sair do menu Inicial)
            sair = True
            print('='*30)
            print('     FINALIZANDO SISTEMA     ')
            print('='*30)
            break

        if escolhaInicial == 1: #condicional que avalia o resultado da função (menuInicial) caso vale 1(Sou Proprietario)
            escolhaProprietario = menuProprietario() #função do menu proprietario
            if escolhaProprietario == 0: #condicional que avalia o resultado da função (menuProprietario) caso vale 0(Voltar para o Menu Inicial)
                print('='*30)
                print('RETORNANDO PARA O MENU INICIAL')
                print('='*30)
                break
            elif escolhaProprietario == 1: #condicional que avalia o resultado da função (menuProprietario) caso vale 1(Atualizar imóveis )
                while True:
                    ProprietarioAtualizar = menuProprietarioAtualizar()
                    if ProprietarioAtualizar == 0:
                        print('='*30)
                        print('RETORNANDO PARA O MENU PROPRIETÁRIO')
                        print('='*30)
                        break
                    elif ProprietarioAtualizar == 1:
                        print('-'*40)
                        AdicionarImovel(regPro, regImo)
            elif  escolhaProprietario == 2: #condicional que avalia o resultado da função (menuProprietario) caso vale 2(Meus Imóveis)
                meuImovel(regImo,regPro)

        elif escolhaInicial == 2: #condicional que avalia o resultado da função (menuInicial) caso vale 1(Sou Corretor)
            escolhaCorretor = menuCorretor() #função do menu Corretor
            if escolhaCorretor == 0: #condicional que avalia o resultado da função (menuCorretor) caso vale 0(Voltar para o Menu Inicial)
                print('='*30)
                print('RETORNANDO PARA O MENU INICIAL')
                print('='*30)
                break
        
        elif escolhaInicial == 3: #condicional que avalia o resultado da função (menuInicial) caso vale 3(Sou Cliente)
            escolhaCliente = menuCliente() #função do menu Cliente
            if escolhaCliente == 0: #condicional que avalia o resultado da função (menuCorretor) caso vale 0(Voltar para o Menu Inicial)
                print('='*30)
                print('RETORNANDO PARA O MENU INICIAL')
                print('='*30)
                break
    if sair == True:
        break