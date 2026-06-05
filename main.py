from operations import add_user, list_users, update_user, delete_user

user_list = [
    {"id": 1, "name": "Juan", "email": "juan@gmail.com", "dni": "40111222"},
    {"id": 2, "name": "Maria", "email": "maria@gmail.com", "dni": "38333444"},
    {"id": 3, "name": "Pedro", "email": "pedro@gmail.com", "dni": "35555666"},
    {"id": 4, "name": "Ana", "email": "ana@gmail.com", "dni": "42777888"},
    {"id": 5, "name": "Luis", "email": "luis@gmail.com", "dni": "39999000"}
]

def main():
    while True:

        print("\n===== GESTIÓN DE USUARIOS =====")
        print("1. Agregar usuario")
        print("2. Listar usuarios")
        print("3. Modificar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")
        try:
            option = int(input("Ingrese una opción: "))

        except ValueError:
            print("Error: ingrese un número")
            continue

        match option:
            case 1:
                add_user(user_list)
            case 2:
                list_users(user_list)
            case 3:
                update_user(user_list)
            case 4:
                delete_user(user_list)
            case 5:
                print("Saliendo...")
                break
            case _:
                print("Opción incorrecta")

if __name__ == "__main__":
    main()