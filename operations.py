from validations import *

next_id = 6



def add_user(user_list):
    
    global next_id 

    name = get_name("Ingrese el nombre: ")
    email = get_unique_email("Ingrese el email: ", user_list)
    dni = get_dni("Ingrese el DNI (sin puntos): ")

    user = {
        "id": next_id,
        "name": name,
        "email": email,
        "dni": dni
    }

    user_list.append(user)
    next_id += 1
    print("Usuario agregado")
    print_user_card(user)



def delete_user(user_list):
    if len(user_list) == 0:
        print("No hay usuarios")
        return

    list_users(user_list)
    user = get_user_by_id("\nIngrese el ID a eliminar: ", user_list)
    
    message = f"¿Seguro que desea eliminar a {user['name']}? (s/n): "
    if get_confirmation(message):
        user_list.remove(user)
        print("Usuario eliminado")
    else:
        print("Operación cancelada")
    return

  


def update_user(user_list):

    list_users(user_list)
    user = get_user_by_id("Ingrese el ID a modificar: ", user_list)

    new_name = get_name("Nuevo nombre (ENTER para no cambiar): ", allow_empty=True)
    if new_name != "":
        user["name"] = new_name

    new_email = get_email("Nuevo email (ENTER para no cambiar): ", allow_empty=True)
    if new_email != "":
        user["email"] = new_email

    new_dni = get_dni("Nuevo DNI (sin puntos, ENTER para no cambiar)): ", allow_empty=True)
    if new_dni != "":
        user["age"] = new_dni
    
    print("Usuario modificado")
    print_user_card(user)
    return

       
def list_users(user_list):
    if len(user_list) == 0:
        print("No hay usuarios registrados.")
        return

    print("\n" + "="*50)
    print("ID | NOMBRE | DNI | EMAIL")
    print("-" * 50)
    
    for user in user_list:

        user_id = user["id"]
        name    = user["name"]
        dni     = user["dni"]
        email   = user["email"]
        
     
        print(f"{user_id} | {name} | {dni} | {email}")
        
    print("="*50 + "\n")
