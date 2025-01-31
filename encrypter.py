from cryptography.fernet import Fernet

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_arquivo:
        chave_arquivo.write(chave)

def criptografar_arquivo(nome_arquivo):
    with open("chave.key", "rb") as chave_arquivo:
        chave = chave_arquivo.read()

    f = Fernet(chave)

    with open(nome_arquivo, "rb") as arquivo:
        conteudo = arquivo.read()

    conteudo_criptografado = f.encrypt(conteudo)

    with open(nome_arquivo + ".enc", "wb") as arquivo_criptografado:
        arquivo_criptografado.write(conteudo_criptografado)

    print(f"O arquivo '{nome_arquivo}' foi criptografado com sucesso!")

gerar_chave()

nome_arquivo = input("Digite o nome do arquivo a ser criptografado: ")
criptografar_arquivo(nome_arquivo)