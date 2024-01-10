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
    print(texto)
    print()

def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de Restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que você deseja cadastrar: ')

    restaurantes.append(nome_do_restaurante)
    
    print(f'\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    menu_principal()

def listar_restaurante():
    exibir_subtitulo('Lista de restaurantes cadastradados: ')

    for i in restaurantes:
        print(f'- {i}')

    menu_principal()

def ativar_restaurante():
    exibir_subtitulo('Ativar restaurantes: ')
    
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
    print('3. Ativar Restaurante')
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
                ativar_restaurante()
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