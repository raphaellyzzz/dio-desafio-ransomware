from cryptography.fernet import Fernet

def descriptografar_arquivo(nome_arquivo_criptografado):
    with open("chave.key", "rb") as chave_arquivo:
        chave = chave_arquivo.read()

    f = Fernet(chave)

    with open(nome_arquivo_criptografado, "rb") as arquivo_criptografado:
        conteudo_criptografado = arquivo_criptografado.read()

    conteudo_descriptografado = f.decrypt(conteudo_criptografado)

    nome_arquivo_original = nome_arquivo_criptografado.replace(".enc", "")
    with open(nome_arquivo_original, "wb") as arquivo_original:
        arquivo_original.write(conteudo_descriptografado)

    print(f"O arquivo '{nome_arquivo_criptografado}' foi descriptografado com sucesso!")

nome_arquivo_criptografado = input("Digite o nome do arquivo a ser descriptografado (com .enc): ")
descriptografar_arquivo(nome_arquivo_criptografado)