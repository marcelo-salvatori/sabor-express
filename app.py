import os

restaurantes = []

def menu_principal():
    '''
    Retorna o usuário o menu principal
    '''
    input('\nAperte enter para voltar ao menu principal')
    main()   

def exibir_subtitulo(texto):
    '''
    Limpa a tela e exibe o subtítulo que cada submenu do programa.
    
    - Argumentos:
        texto: String
    '''
    os.system('cls')
    linha = '=' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_restaurante():
    '''
    Recebe inputs do usuário para cadastra um novo restaurante e adiciona os dados num dicionário

    - Input:
        Nome do restaurante: String
        Categoria do restaurante: String
    
    '''
    exibir_subtitulo('Cadastro de Restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que você deseja cadastrar: ')
    categoria_do_restaurante = input('Digite a categoria a qual esse restaurante pertence: ')

    dados_do_restaurante = {'nome':nome_restaurante, 'categoria':categoria_do_restaurante, 'ativo':False}

    restaurantes.append(dados_do_restaurante)
    
    print(f'\nO restaurante {nome_restaurante} foi cadastrado com a categoria {categoria_do_restaurante}, com o status inativo. Não se esqueça de ativá-lo.')
    menu_principal()

def listar_restaurante():
    '''
    Mostra um sub-menu com uma tabela contendo informações de todos os restaurantes cadastrados
    '''
    exibir_subtitulo('Lista de restaurantes cadastradados: ')

    cabeçalho = f'{'Nome'.ljust(20)}|{'Categoria'.ljust(20)}|Status'
    separador = '-' * (len(cabeçalho) + 1)
    print(cabeçalho)
    print(separador)


    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        restaurante_ativo = 'ativo'if restaurante['ativo'] == True else 'inativo'

        print(f'{nome_restaurante.ljust(20)}|{categoria_restaurante.ljust(20)}|{restaurante_ativo}')

    menu_principal()

def alternar_status_restaurante():
    '''
    Alterna o status entre \'ativo\' e \'inativo\' de algum restaurante cadastrado

    -Input:
        Nome do restaurante: String
    '''
    exibir_subtitulo('Alternar Status do restaurante')

    nome_restaurante = input('Digite o nome do restaurante que você deseja alternar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem_status = f'O restaurante {restaurante['nome']} foi ATIVADO com sucesso' if restaurante['ativo'] == True else f'O restaurante {restaurante['nome']} foi DESATIVADO com sucesso'
            print(mensagem_status)

    if not restaurante_encontrado:
        print('O Restaurante não foi encontrado')
    
    menu_principal()

def finalizar_app():
    os.system('cls')
    print('Você saiu do programa\n')

def exibir_nome_programa():

    print("""
╭━━╮╱╱╭╮╱╱╱╱╱╭━╮╱╱╱╱╱╱╱╭━┳━╮
┃━━╋━╮┃╰┳━┳┳╮┃┳╋┳┳━┳┳┳━┫━┫━┫
┣━━┃╋╰┫╋┃╋┃╭╯┃┻╋┃┫╋┃╭┫┻╋━┣━┃
╰━━┻━━┻━┻━┻╯╱╰━┻┻┫╭┻╯╰━┻━┻━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
""")

def exibir_opcoes():
    '''
    Exibe um menu de opções que o usuário pode selecionar para exercutar as funções do programa
    '''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar status do Restaurante')
    print('4. Sair')

def opcao_invalida():
    '''
    Função que faz o usuário retornar ao menu principal, caso escolha uma opção inválida
    '''
    print('Opção inválida!\n')
    menu_principal()

def escolher_opcao():
    '''
    Recebe o input de usuário e executa a função de acordo com a opção selecionada.
    Caso o usuário digita algo que não seja um número inteiro, ou que não seja um número de 1 a 4, ele retornará ao menu principal
    '''
    try:
        opcao_escolhida = int(input('\nEscolha uma opção: '))

        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurante()
            case 3:
                alternar_status_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()