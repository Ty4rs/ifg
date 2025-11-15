from registro import *
def meuImovel(registroImovel,registroProprietario): #Apresenta os imóveis do Proprietário
    while True:
        achou = False
        analise = input('Me fale o seu ID de Proprietário (0 para voltar para o Menu Proprietário): ')
        if analise == '0':
            break
        for i in range (len(registroProprietario)):
            if analise == registroProprietario[i].cod: #Verifica se o Proprietário existe
                print ('PROPRIETÁRIO ENCONTRADO!')
                achou = True
                quantidadeImovel = len(registroProprietario[i].imovelPossuido)
                if quantidadeImovel != 0:
                    print(f"Segue os imóveis do proprietário {registroProprietario[i].nome}:")
        
                    for j in registroProprietario[i].imovelPossuido:
                        print(registroImovel[i])
                else:
                    print("Nenhum imóvel cadastrado!")
        if achou == True:
            break
        
        if achou == False:
            print ('-'*30)
            print ('CÓDIGO DO PROPRIETÁRIO ESTÁ INCORRETO ')
            print ('-'*30)

def AdicionarImovel(registroProprietario, registroImovel):
    while True:
        achou = False
        sair = False
        analise = input('Me fale o seu ID de Proprietário (0 para voltar para o Menu Proprietário): ')
        if analise == '0':
            break
        for i in range (len(registroProprietario)):
            if analise == registroProprietario[i].cod: #Verifica se o Proprietário existe
                print ('PROPRIETÁRIO ENCONTRADO!')
                achou = True
                quant = len(registroImovel)
                registroImovel.append(IMOVEL())
                registroImovel[quant].codigoImovel = quant+1
                tipoImo = input ('Me fale que tipo o imóvel vai ser comercializado (Aluguel/Venda): ').lower()[0]
                if tipoImo == 'a':
                    registroImovel[quant].tipo = 'Aluguel'
                    registroImovel[quant].status = 'À Alugar'
                if tipoImo == 'v':
                    registroImovel[quant].tipo = 'Venda'
                    registroImovel[quant].status = 'À Alugar'
                registroImovel[quant].rua = input ('Me fale a Rua/Avenida que o imóvel está localizado: ').lower
                registroImovel[quant].setor = input ('Me fale qual o setor/Bairro que o imóvel está localizado: ').lower
                registroImovel[quant].NCasa = input ('Me fale o número do imóvel (caso não tenha coloque sn): ').lower
                registroImovel[quant].tamanho = float(input ('Me fale o tamanho total do imóvel em m²: '))
                registroImovel[quant].quarto = int (input ('Me fale quantos cômodos (Excluindo somente os banheiros) o imóvel contêm: '))
                for i in range (registroImovel[quant].quarto):
                    tamCom = float(input(f'Me fale o tamanho do {i+1}° cômodo em m²: '))
                    registroImovel[quant].tamanhoQuarto.append(tamCom)
                registroImovel[quant].banheiro = int(input ('Me fale a quantos banheiros a casa contêm: '))
                for i in range (registroImovel[quant].banheiro):
                    tamBan = float(input(f'Me fale o tamanho do {i+1}° banheiro em m²: '))
                    registroImovel[quant].tamanhoBanheiro.append(tamBan)
                    sair = True
                registroProprietario.imovelPossuido.append(registroImovel[quant].codigoImovel)           
                print ('Todos os dados do imóvel foi cadastrado')
                print (f'O código desse imóvel é {registroImovel[quant].codigoImovel}')
                print ('='*50)
                print ('VOLTANDO PARA O MENU PROPRIETÁRIO')
                print ('='*50)
                break
        if achou == False:
            print ('*'*50)
            print ('PROPRIETÁRIO NÃO ENCONTRADO')
            print ('*'*50)
        if sair == True:
            break
    
def validarCpf(cpf: str) -> bool:
    # Remove pontos e traços
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais (CPF inválido)
    if cpf == cpf[0] * 11:
        return False

    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    digito1 = 0 if digito1 == 10 else digito1

    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11
    digito2 = 0 if digito2 == 10 else digito2

    # Compara com os dígitos originais
    return cpf[-2:] == f"{digito1}{digito2}"


'''# Resultado
cpf_input = "04569258131"
if validarCpf(cpf_input):
    print("CPF válido")
else:
    print("CPF inválido")'''