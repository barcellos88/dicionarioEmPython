def perguntar():
    return input("O que deseja realizar ?\n" +
              "<I> - Para Inserir um usuário\n" +
              "<P> - Para Psquisar um usuário\n" +
              "<E> - Para Excluir um usuário\n" +
              "<L> - Para Listar um usuáio: ").upper()

#upper é utilizado para deixar qualquer digitaçao maiuscula

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                   input("Digite a última data de acesso: "),
                                                   input("Qual a última estação acessada: ").upper()]