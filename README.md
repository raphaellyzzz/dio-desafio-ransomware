# Desafio

- **encrypter.py**: Criptografa arquivo, tornando-o ilegível sem a chave de descriptografia.
- **decrypter.py**: Descriptografa arquivo, recuperando seu conteúdo original.

## 1 passo 
É necessário baixar a biblioteca cryptography, use o comando no terminal:

`pip install cryptography`

## Criptografar 
Para criptografar é necessário executar o script **encrypter.py** e passar o caminho do arquivo que deseja criptografar, renomeando com a extensão .encrypted

`python encrypter.py arquivo.txt`

## Descriptografar
É necessário executar o script decrypter.py, passando o arquivo criptografado.

`python decrypter.py arquivo.txt.encrypted`
