from Crypto.PublicKey import RSA
import sys
from getpass import getpass

def CriarParDeChaves(tamanho=2048,senha=None):
    """
    -
    Função para criar um par de chaves utilizando o RSA
    tamanho: tamanho, em bits, da chave. Padrão = 2048
    senha: senha que será usada para usar a chave
    """
    global chavePrivada
    global chavePublica

    chave = RSA.generate(tamanho)
    chavePrivada = chave.export_key('PEM',passphrase=senha)
    chavePublica = chave.public_key().export_key('PEM')

def GetChavePrivada():
    """
    -
    Função que retorna a chave privada, caso exista.
    """
    if(chavePrivada is None):
        print("Chave publica não foi gerada")
    else:
        return chavePrivada

def GetChavePublica():
    """
    -
    Função que retorna a chave privada, caso exista.
    """
    if(chavePublica is None):
        print("Chave publica não foi gerada")
    else:
        return chavePublica

def GerarArquivo(s):
    CriarParDeChaves(2048,s)
    arquivoChavePrivada = open("chavePrivada.pem","wb")
    arquivoChavePrivada.write(GetChavePrivada())
    arquivoChavePrivada.close()
    arquivoChavePublica = open("chavePublica.pem","wb")
    arquivoChavePublica.write(GetChavePublica())
    arquivoChavePublica.close()
    print("'chavePrivada.pem' e 'chavePublica.pem' foram gerados no dirétorio atual.")

def Iniciar():
    Main()

def Main():
    print("Bem vindo ao gerador de chaves.")
    #senha = input("Digite a senha que você quer usar na chave privada: ")
    senha = getpass("Digite a senha que você quer usar na chave privada:\n")
    GerarArquivo(senha)

if(len(sys.argv)>1):
    argumento = sys.argv[1]
    senha = sys.argv[2]

Iniciar()