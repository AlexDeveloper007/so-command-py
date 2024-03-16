import win32net

def list_users_detailed():
    users = []
    resume_handle = 0

    while True:
        # Obtem a lista de usuários. 
        #level = 1 retorna informações detalhadas do usuário.
        result, total_entries, resume_handle = win32net.NetUserEnum(None, 1, 0, resume_handle)
        for user in result:
            # Usei .get() para evitar KeyError se a chave não existir
            user_info = {
                'name': user.get('name'),
                'priv_level': user.get('priv'),  # Nível de privilégio: 0 = Convidado, 1 = Usuário, 2 = Administrador
                #Outras informacoes poderiam ser adicionadas, como: user_id, home_dir e etc
            }
            users.append(user_info)

        if not resume_handle:
            break

    return users

# Listar os usuários detalhadamente e imprimir as informações de cada um
for user in list_users_detailed():
    print(f"Name: {user['name']}, Privilege Level: {user['priv_level']}")

