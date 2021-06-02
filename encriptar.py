from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from sys import argv
def Encriptar(arquivosPraEncriptar,caminhoChave,caminho):
    """
    -
    
    Função para encriptar um texto.
    arquivosPraEncriptar: variavel onde se encontra as senhas
    caminhoChave: caminho onde se encontra a chave
    caminho: caminho onde vai salvar o arquivo
    """
    texto = str(arquivosPraEncriptar).encode("utf-8")
    # Texto a ser encriptado, transformado em bytes

    temp = open(caminho,"wb")
    # Leu o arquivo onde vai ser salvo as senhas e marcou que vai ser salvo em bytes

    chave = RSA.import_key(open(caminhoChave).read())
    # Leitura e importação da chave que sera usada para encriptar

    chaveSessao = get_random_bytes(16)
    #

    cifraRSA = PKCS1_OAEP.new(chave)
    #

    chaveSessaoEncriptada = cifraRSA.encrypt(chaveSessao)
    #

    cifraAES = AES.new(chaveSessao,AES.MODE_EAX)
    #

    textoCrifrado, tag = cifraAES.encrypt_and_digest(texto)
    #

    [temp.write(x) for x in (chaveSessaoEncriptada,cifraAES.nonce,tag,textoCrifrado)]
    #

    temp.close()
    # Apaga o arquivo da memoria

if(len(argv)>1):
    Encriptar(argv[1],argv[2],argv[3])
else:
    print("Você deve passar os arquivos como argumento.\nEXEMPLO:\nencriptar.py caminhoArquvivoParaEncriptar caminhoDaChave caminhoDaSaida")