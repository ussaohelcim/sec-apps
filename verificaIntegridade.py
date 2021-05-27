"""
Programa para verficar a integridade de algo.
"""
from os import pipe
import sys
from Crypto.Hash import SHA512

def GetHash(caminho):
    arquivo = open(caminho,'rb')
    h = SHA512.new()
    h.update(arquivo.read())
    arquivo.close()
    return h.hexdigest()

def Comparar():
    print()

def Help():
    print("""
uso: verificaIntegridade.py [arquivo] [SHA512]

Programa para verificar a integridade de um arquivo.

arquivo     Arquivo que você quer verificar o SHA512.
SHA512      SHA512 do arquivo original que você já tem e quer usar para verificar a integridade do arquivo.
""")

def Iniciar(a):
    if(len(a)<2):
        Help()
    else:
        if(a[1] == '--c'):
            print(GetHash(a[2]).upper())

Iniciar(sys.argv)