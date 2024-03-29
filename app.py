import os

restaurantes = [{'nome': 'Parça', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Pizza Suprema', 'categoria': 'pizza', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}]


def exebir_nome_programa():
    ''' Exebir nome estilizado do programa na tela'''
    print("""
      
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)


def exebir_opcao():
    '''Exebir as opção disponiveis no menu principal '''
    print('1. Cadastrar Restaurantes')
    print('2. Listar Restaurante')
    print('3. Alternar estado do Restaurante')
    print('4. Sair\n')


def finalizar_app():
    '''Exibir mensagem de finalização de aplicativo'''
    exibir_subtitulo('Finalizando o app')


def voltar_ao_menu_principal():
    '''
     Solicita uma tecla para voltar ao menu principal 

    Outputs:
    - Retorna ao menu principal
    '''
    input('\nDigite uma Tecla para voultar ao menu ')
    main()


def exibir_subtitulo(texto):
    ''' Exibir um subtitulo estizado na tela


          Inputs:
        - texto: str - O texto do subtítulo
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def opcao_invalida():
    '''Exibir mensagen opção de inválida e retorna ao menu principal

      Outputs:
    - Retorna ao menu principal
    '''
    print('Opção invalida\n')
    voltar_ao_menu_principal()


def cadastrar_novo_restaurante():
    '''Esssa função é responsável por cadastrar um novo restaurante

    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input(
        'Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(
        f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_restaurante = {'nome': nome_do_restaurante,
                         'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    '''Altera o estado ativo/desativado de um restaurante 

      Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input(
        'Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso ' if restaurante[
                'ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()


def listar_restaurantes():
    ''' Lista os restaurantes presentes na lista 

        Outputs:
        - Exibe a lista de restaurantes na tela
        '''
    exibir_subtitulo('Listando todos os Restaurantes')
    nome = 'Nome do restaurante'.ljust(23)
    categoria_restaurante = 'Categoria'.ljust(20)
    print(f'{nome} | {categoria_restaurante} | Status')
    for restaurante in restaurantes:
        nome_resturante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f' - {nome_resturante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()


def escolher_opcao():
    '''
     Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    opcao_escolhida = int(input('Escolha uma opção: '))
    # opcao_escolhida = int(opcao_escolhida)

    try:
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()

        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    ''' Função principal que inicia o programa'''
    os.system('cls')
    exebir_nome_programa()
    exebir_opcao()
    escolher_opcao()


if __name__ == '__main__':
    main()
