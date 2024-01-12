"""
feat: uma nova feature (recurso) que você está adicionando a uma aplicação específica ;
fix: a resolução de um bug;
style: recurso e atualizações relacionadas à estilização;
refactor: refatoração de uma seção específica da base de código;
test: tudo o que for relacionado a testes;
docs: tudo o que for relacionado à documentação;
chore: manutenção regular do código. (Você também pode usar emojis para representar os tipos de commit).
"""

import os

restaurantes = []

def menu_principal():
    input('\nAperte enter para voltar ao menu principal')
    main()   

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '=' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de Restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que você deseja cadastrar: ')
    categoria_do_restaurante = input('Digite a categoria a qual esse restaurante pertence: ')

    dados_do_restaurante = {'nome':nome_restaurante, 'categoria':categoria_do_restaurante, 'ativo':False}

    restaurantes.append(dados_do_restaurante)
    
    print(f'\nO restaurante {nome_restaurante} foi cadastrado com a categoria {categoria_do_restaurante}, com o status inativo. Não se esqueça de ativá-lo.')
    menu_principal()

def listar_restaurante():
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
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar status do Restaurante')
    print('4. Sair')

def opcao_invalida():
    print('Opção inválida!\n')
    menu_principal()

def escolher_opcao():
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

"""
Beautiful is better than ugly.\

Explicit is better than implicit.\

Simple is better than complex.\

Complex is better than complicated.\

Flat is better than nested.\

Sparse is better than dense.\

Readability counts.\

Special cases aren't special enough to break the rules.\

Although practicality beats purity.\

Errors should never pass silently.\

Unless explicitly silenced.\

In the face of ambiguity, refuse the temptation to guess.\

There should be one-- and preferably only one --obvious way to do it.\

Although that way may not be obvious at first unless you're Dutch.\

Now is better than never.\

Although never is often better than right now.\

If the implementation is hard to explain, it's a bad idea.\

If the implementation is easy to explain, it may be a good idea.\

Namespaces are one honking great idea -- let's do more of those!\
"""