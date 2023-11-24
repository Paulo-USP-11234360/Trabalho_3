import hashlib

def get_password_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def check_password(user_password, stored_hashed_password):
    hashed_user_password = hash_password(user_password)
    return hashed_user_password == stored_hashed_password

if __name__ == "__main__":
    # Caminhos dos arquivos de senha
    password_file = "../senha.txt"
    hashed_password_file = "../senha_encriptada.txt"

    # Leia a senha armazenada e a senha criptografada do arquivo
    stored_password = get_password_from_file(password_file)
    stored_hashed_password = get_password_from_file(hashed_password_file)

    # Opção 1: Exibir a senha ao usuário
    print(f"A senha armazenada é: {stored_password}")
    user_password = input("Digite a senha para verificar: ")


    if check_password(user_password, stored_hashed_password):
        print("Senha correta!")
    else:
        print("Senha incorreta!")