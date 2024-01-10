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

def cadastrar_restaurante():
    print('Cadastrar restaurantes: ')

def listar_restaurante():
    print('Listar restaurantes: ')

def ativar_restaurante():
    print('Ativar restaurantes: ')

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

def escolher_opcao():
    opcao_escolhida = int(input('\nEscolha uma opção: '))
    print(f'A opção escolhida foi: {opcao_escolhida}.')

    match opcao_escolhida:
        case 1:
            cadastrar_restaurante()
        case 2:
            listar_restaurante()
        case 3:
            ativar_restaurante()
        case 4:
            finalizar_app()

def main():
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