from funcoes import adicionar_contato, carregar_contatos, salvar_contatos, editar_contato, excluir_contato, exibir_contatos
operacao = 0

while operacao != 5:
    operacao = int(input("Selecione a opção desejada:\n[1] Adicionar novo contato\n[2] Editar contatos\n[3] Excluir contato\n[4] Ver contatos\n[5] Encerrar programa\n"))
    if operacao == 1:
        adicionar_contato()
    elif operacao == 2:
        editar_contato()
    elif operacao == 3:
        excluir_contato()
    elif operacao == 4:
        exibir_contatos()
    elif operacao == 5:
        print("Encerrando programa...")
    else:
        print("Op. Inválida!")
