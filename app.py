import os

restaurantes = [{'nome':'parça','categoria':'Japonesa','ativo': False},
                {'nome':'Pizza Suprema','categoria':'pizza','ativo':True},
                {'nome':'cantina','categoria':'Italiano','ativo': False}]


def exebir_nome_programa():
    print("""
      
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)


def exebir_opcao():
    print('1. Cadastrar Restaurantes')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')


def finalizar_app():
    exibir_subtitulo('Finalizando o app')
    


def voltar_ao_menu_principal():
    input('\nDigite uma Tecla para voultar ao menu ')
    main()


def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()


def opcao_invalida():
    print('Opção invalida\n')
    voltar_ao_menu_principal()


def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input(
        'Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulo('Listando todos os Restaurantes')
    for restaurante in restaurantes:
        nome_resturante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f' - {nome_resturante} | {categoria} | {ativo}')

    voltar_ao_menu_principal()


def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    # opcao_escolhida = int(opcao_escolhida)

    try:
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurantes')

        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exebir_nome_programa()
    exebir_opcao()
    escolher_opcao()


if __name__ == '__main__':
    main()
