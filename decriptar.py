from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import getpass
from sys import argv
from gerenciadorDeSenhas import pmDecriptador as dcpt
def Decriptar(arquivoEncriptado,caminhoChave,caminhoSaida):
    global noConsole
    senha = getpass.getpass("Digite a senha da chave:\n")
    #senha = input("Digite a senha da chave:\n")

    arquivo = (open(arquivoEncriptado,"rb"))
    chavePrivada = RSA.import_key(open(caminhoChave).read(),senha)
    
    chaveSessaoEncriptada, nonce, tag, textoCifrado = \
        [arquivo.read(x) for x in (chavePrivada.size_in_bytes(),16,16,-1)]
    cifraRSA = PKCS1_OAEP.new(chavePrivada)
    chaveSessao = cifraRSA.decrypt(chaveSessaoEncriptada)

    cifraAES = AES.new(chaveSessao,AES.MODE_EAX,nonce)
    dado = cifraAES.decrypt_and_verify(textoCifrado,tag)

    if(caminhoSaida == "-n"):
        print(dado.decode("utf-8"))
    else:
        saida = open(caminhoSaida,'w')
        saida.write(dado.decode("utf-8"))
        saida.close()
        print(caminhoSaida+" foi gerado.")


if(len(argv)>1):
    Decriptar(argv[1],argv[2],argv[3])
else:
    print("Você deve passar os arquivos como argumento.\nEXEMPLO:\ndecriptar.py caminhoArquvivoParaDecriptar caminhoDaChave caminhoDaSaida\nOU\ndecriptar.py caminhoArquvivoParaDecriptar caminhoDaChave -n")
