from operaciones import agregar_usuario, listar_usuarios, modificar_usuario, borrar_usuario
agenda = [
    {"id": 1, "nombre": "Juan", "email": "juan@gmail.com", "edad": 20},
    {"id": 2, "nombre": "Maria", "email": "maria@gmail.com", "edad": 25},
    {"id": 3, "nombre": "Pedro", "email": "pedro@gmail.com", "edad": 30},
    {"id": 4, "nombre": "Lucia", "email": "lucia@gmail.com", "edad": 22},
    {"id": 5, "nombre": "Carlos", "email": "carlos@gmail.com", "edad": 28}
]

def main():
    while True:

        print("\n===== GESTIÓN DE agenda =====")
        print("1. Agregar usuario")
        print("2. Listar agenda")
        print("3. Modificar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")

        try:
            opcion = int(input("Ingrese una opción: "))

        except ValueError:
            print("Error: ingrese un número")
            continue


        match opcion:

            case 1:
                agregar_usuario(agenda)

            case 2:
                listar_usuarios(agenda)

            case 3:
                modificar_usuario(agenda)

            case 4:
                borrar_usuario(agenda)

            case 5:
                print("Saliendo...")
                break

            case _:
                print("Opción incorrecta")

if __name__ == "__main__":
    main()