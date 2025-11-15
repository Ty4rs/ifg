def menuInicial ():
    while True: #Repetição para caso a pessoa não escolha uma opção possível
        print (' --------- MENU INICIAL ----------')
        print (' ----------------------------------')
        print ('| Escolha uma das opções a seguir: |')
        print (' ----------------------------------')
        print ('| 0. Sair do menu inicial          |')
        print ('| 1. Sou Proprietário              |')
        print ('| 2. Sou Corretor                  |')
        print ('| 3. Sou Cliente                   |')
        print (' ----------------------------------')

        escolha = int(input('Informe a opção desejada: ')) #input para a escolha do menu
        if 0 <= escolha <= 3:
            print ('MW'*30) 
            return escolha
        else:
            print ('-OPÇÃO INVÁLIDA-')
            print ('-TENTE NOVAMENTE-')
        print ('MW'*30)    

def menuProprietario():
    while True: #Repetição para caso a pessoa não escolha uma opção possível
        print (' ------- MENU PROPRIETARIO --------')
        print (' ----------------------------------')
        print ('| Escolha uma das opções a seguir: |')
        print (' ----------------------------------')
        print ('| 0. Voltar para o Menu Inicial    |')
        print ('| 1. Atualizar imóveis             |')
        print ('| 2. Meus Imóveis                  |')
        print (' ----------------------------------')

        escolha = int(input('Informe a opção desejada: ')) #input para a escolha do menu
        if 0 <= escolha <= 2: #condicional caso o usuário escolha uma oção possível (0,1 2)
            print ('MW'*30) 
            return escolha #A função retorna valendo a escolha do usuário
        else: #condicional caso o usuário não escolha uma opção possível, retornando para o inicio da função
            print ('-OPÇÃO INVÁLIDA-')
            print ('-TENTE NOVAMENTE-')
        print ('MW'*30)

def menuProprietarioAtualizar():
    while True: #Repetição para caso a pessoa não escolha uma opção possível
        print (' --------- ATUALIZAR IMÓVEL ---------')
        print (' ------------------------------------')
        print ('| Escolha uma das opções a seguir:   |')
        print (' ------------------------------------')
        print ('| 0. Voltar para o Menu Proprietário |')
        print ('| 1. Adicionar Imóvel                |')
        print ('| 2. Excluir Imóvel                  |')
        print ('| 3. Modificar Imóvel                |')
        print (' ------------------------------------')

        escolha = int(input('Informe a opção desejada: ')) #input para a escolha do menu
        if 0 <= escolha <= 2: #condicional caso o usuário escolha uma oção possível (0,1 2)
            print ('MW'*30) 
            return escolha #A função retorna valendo a escolha do usuário
        else: #condicional caso o usuário não escolha uma opção possível, retornando para o inicio da função
            print ('-OPÇÃO INVÁLIDA-')
            print ('-TENTE NOVAMENTE-')
        print ('MW'*30)

def menuCorretor():
    while True: #Repetição para caso a pessoa não escolha uma opção possível
        print (' --------- MENU CORRETOR ----------')
        print (' ----------------------------------')
        print ('| Escolha uma das opções a seguir: |')
        print (' ----------------------------------')
        print ('| 0. Voltar para o Menu Inicial    |')
        print ('| 1. Cadastrar Imóvel              |')
        print ('| 2. Todos os Imóveis              |')
        print (' ----------------------------------')
        
        escolha = int(input('Informe a opção desejada: ')) #input para a escolha do menu
        if 0 <= escolha <= 2: #condicional caso o usuário escolha uma oção possível (0,1 2)
            print ('MW'*30) 
            return escolha #A função retorna valendo a escolha do usuário
        else: #condicional caso o usuário não escolha uma opção possível, retornando para o inicio da função
            print ('-OPÇÃO INVÁLIDA-')
            print ('-TENTE NOVAMENTE-')
        print ('MW'*30)

def menuCliente():
    while True: #Repetição para caso a pessoa não escolha uma opção possível
        print (' --------- MENU CLIENTE -----------')
        print (' ----------------------------------')
        print ('| Escolha uma das opções a seguir: |')
        print (' ----------------------------------')
        print ('| 0. Cadastrar Cliente             |')
        print ('| 1. Voltar para o Menu Inicial    |')
        print ('| 2. Buscar Imóveis                |')
        print ('| 3. Ver todos os Imóveis          |')
        print (' ----------------------------------')
        
        escolha = int(input('Informe a opção desejada: ')) #input para a escolha do menu
        if 0 <= escolha <= 3: #condicional caso o usuário escolha uma oção possível (0,1 2)
            print ('MW'*30) 
            return escolha #A função retorna valendo a escolha do usuário
        else: #condicional caso o usuário não escolha uma opção possível, retornando para o inicio da função
            print ('-OPÇÃO INVÁLIDA-')
            print ('-TENTE NOVAMENTE-')
        print ('MW'*30)