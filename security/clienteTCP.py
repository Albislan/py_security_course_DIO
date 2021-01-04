import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou!!!")
        print("Erro: {}".format(e))
        sys.exit()

    print("socket criado com sucesso!")


    HostAlvo = input("Digite o Host ou IP`a ser conectado: \n")
    portaAlvo = input("Digite a porta a ser conectada: \n")

    try:
        s.connect((HostAlvo, int(portaAlvo)))
        print("Cliente TCP conectado com sucesso no Host: " + HostAlvo + " e na porta: " + portaAlvo)
        s.shutdown(2)
    except socket.error as e:
        print("A conexão com o Host: " + HostAlvo + " e a porta: " + portaAlvo + " Falhou") 
        print("Erro: {}".format(e))
        sys.exit()


if __name__ == "__main__":
    main()                   