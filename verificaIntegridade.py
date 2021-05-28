"""
Programa para verficar a integridade de algo, utilizando o SHA512.
"""
import sys # Importação da biblioteca de sistema, para pegar os argumentos do stdin
from Crypto.Hash import SHA512 # Importação das funções de SHA512 da biblioteca Hash de dentro do PyCryptodome

def GetHash(caminho): # Função que retorna o hash de um arquivo
    arquivo = open(caminho,'rb') # Lê os binarios do arquivo e salva na memoria
    hash = SHA512.new() # Cria um hash SHA512 vazio
    hash.update(arquivo.read()) # Lê o arquivo na memoria e atualiza o hash com o arquivo
    arquivo.close() # Fecha o arquivo na memoria
    return hash.hexdigest() # Retorna o hash pra quem chamou, já disgestado

a = sys.argv # Pega os argumentos recebidos no stdin

if(len(a)>1):
    print(GetHash(a[1]).upper()) # 
#