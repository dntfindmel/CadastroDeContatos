import json


def carregar_contatos():
    try:
        with open("contatos.json", "r") as arquivo:
            conteudo = arquivo.read()
            if conteudo.strip():
                return json.loads(conteudo)
            else:
                return {}
    except FileNotFoundError:
        return {}


def salvar_contatos(contatos):
    with open("contatos.json", "w") as arquivo:
        json.dump(contatos, arquivo)


def adicionar_contato():
    dic_contatos = carregar_contatos()

    contato = input("Digite o número que deseja adicionar: ")
    nome = input("Como você deseja salvar este contato? ").capitalize()

    dic_contatos[nome] = contato
    print(f"Contato salvo com sucesso! {nome} - {dic_contatos[nome]}")
    salvar_contatos(dic_contatos)


def editar_contato():
    dic_contatos = carregar_contatos()
    antigo_nome = input("Digite o contato que deseja modificar: ").capitalize()

    if antigo_nome in dic_contatos:
        opcao = int(input("Qual a mudança desejada?\n[1] Modificar nome\n[2] Modificar telefone\n[3] Sair\n"))

        if opcao == 1:
            novo_nome = input(f"Digite um novo nome para {antigo_nome} : ").capitalize()
            dic_contatos[novo_nome] = dic_contatos.pop(antigo_nome)
            print(f"Contato modificado: {novo_nome} - {dic_contatos[novo_nome]}")
        elif opcao == 2:
            novo_telefone = input(f"Digite um novo número para {antigo_nome}: ")
            dic_contatos[antigo_nome] = novo_telefone
            print(f"Contato modificado: {antigo_nome} - {dic_contatos[antigo_nome]}")
        elif opcao == 3:
            return
        else:
            print("Op. inválida!")
    else:
        print(f"O contato {antigo_nome} não foi encontrado.")
    salvar_contatos(dic_contatos)

def excluir_contato():
    dic_contatos = carregar_contatos()
    excluir = input("Digite o nome do contato que deseja excluir: ").capitalize()

    if excluir in dic_contatos:
        confirmacao = input(f"Tem certeza que deseja excluir este contato [S]\[N]? {excluir} ").upper()
        if confirmacao == 'S':
            del dic_contatos[excluir]
            print(f"Contato {excluir} excluído com sucesso!")
            salvar_contatos(dic_contatos)
        elif confirmacao == 'N':
            print(f"O contato {excluir} não foi excluído.")
        else:
            print("Op. Inválida!")
    else:
        print(f"O contato {excluir} não foi encontrado.")


def exibir_contatos():
    dic_contatos = carregar_contatos()

    if dic_contatos:
        print("\nLista de contatos:\n")
        for nome, telefone in dic_contatos.items():
            print(f"{nome} - {telefone}")
    else:
        print("Nenhum contato encontrado.")