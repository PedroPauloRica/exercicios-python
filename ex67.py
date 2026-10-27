while True:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if senha == usuario:
        print("a senha não pode ser igual ao nome de usuário\n")
    else:
        print("Usuário e senha cadastrados com sucesso!")
        break