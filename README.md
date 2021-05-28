# sec-apps
Aplicações de segurança em Python para demonstração da biblioteca PyCryptodome.

## Apresentação
*sec-apps* é um repositorio para demonstrar como fazer aplicações de segurança utilizando Python e o PyCryptodome.

[Informações sobre o seminario]()

## Conteudo
<!-- programa para assinar e verificar assinaturas digitais-->
- programa para verificar a integridade de um arquivo utilizando SHA512
- programa para gerar chaves publicas e privadas
- programa para encriptar ou decriptar arquivo usando chave publica e privada
- programa para gerenciar senhas de forma segura

## Informações
Este repositorio foi feito para ser demonstrado em um seminário, na disciplina de criptografia, da Fatec São Caetano do Sul.

## PyCryptodome
Para mais informações sobre o PyCryptodome acesse:
- Site oficial: https://www.pycryptodome.org/
- Repositório atual, mantido por "Legradin": https://github.com/Legrandin/pycryptodome
- Pagina da biblioteca, no repositório pypi: https://pypi.org/project/pycryptodome/

## Utilizando o PyCryptodome
Primeiro instale o PyCryptodome:
```
pip install pycryptodome
```
Faça o teste da biblioteca para checar se não existe nenhum problema:
```
python3 -m Crypto.SelfTest
```
## Utilizando o verificador de integridade
```python
python3 verificaIntegridade.py arquivo
#0123456789ABCDEF -- a saida será o hash SHA512 do arquivo
```

## Utilizando o gerador de chaves
```python
python3 geradorDeChaves.py
#
```
