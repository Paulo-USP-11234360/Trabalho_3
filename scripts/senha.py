import os
import hashlib
import sys

def get_password_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def check_password(user_password, stored_hashed_password=None):
    if stored_hashed_password is None:
        stored_hashed_password = os.getenv("STORED_HASHED_PASSWORD")
        if stored_hashed_password is None:
            raise ValueError("A variável de ambiente STORED_HASHED_PASSWORD não foi fornecida.")
    
    hashed_user_password = hash_password(user_password)
    return hashed_user_password == stored_hashed_password

if __name__ == "__main__":
    # Obtém o diretório do script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Caminhos dos arquivos de senha
    password_file = os.path.join(script_directory, "senha.txt")
    hashed_password_file = os.path.join(script_directory, "senha_encriptada.txt")

    # Leia a senha armazenada e a senha criptografada do arquivo
    stored_password = get_password_from_file(password_file)
    stored_hashed_password = get_password_from_file(hashed_password_file)

    # Exibe a senha ao usuário
    print(f"A senha armazenada é: {stored_password}")

    # Obtém a senha do argumento de linha de comando
    # if len(sys.argv) != 2:
    #     print("Uso: python senha.py <senha>")
    #     sys.exit(1)

    # user_password = sys.argv[1]

    # if check_password(user_password, stored_hashed_password):
    #     print("Senha correta!")
    # else:
    #     print("Senha incorreta!")
