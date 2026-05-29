from validaciones import *

siguiente_id = 6



def agregar_usuario(agenda):
    
    global siguiente_id 

    nombre = pedir_nombre("Ingrese el nombre: ")
    email = pedir_email_unico("Ingrese el email: ", agenda)
    edad = pedir_edad("Ingrese la edad: ")

    usuario  = {
        "id": siguiente_id,
        "nombre": nombre,
        "email": email,
        "edad": edad
    }

    agenda.append(usuario)
    siguiente_id += 1
    print("Usuario agregado")



def borrar_usuario(agenda):
    if len(agenda) == 0:
        print("No hay agenda")
        return

    listar_usuarios(agenda)

    usuario = pedir_usuario_por_id("\nIngrese el ID a borrar: ", agenda)
    mensaje = f"¿Seguro que desea eliminar a {usuario['nombre']}? (s/n): "
    if pedir_confirmacion(mensaje):
        agenda.remove(usuario)
        print("Usuario eliminado")
    else:
        print("Operación cancelada")

    

def modificar_usuario(agenda):
    if len(agenda) == 0:
        print("No hay agenda")
        return
    
    listar_usuarios(agenda)

    usuario = pedir_usuario_por_id("Ingrese el ID a modificar: ", agenda)
    # NOMBRE
    nuevo_nombre = pedir_nombre("Nuevo nombre (ENTER para no cambiar): ", permite_vacio=True)
    if nuevo_nombre != "":
        usuario["nombre"] = nuevo_nombre

    # EMAIL 
    nuevo_email = pedir_email("Nuevo email (ENTER para no cambiar): ", permite_vacio=True)
    if nuevo_email != "":
        usuario["email"] = nuevo_email

    # EDAD
    nueva_edad = pedir_edad("Nueva edad (ENTER para no cambiar): ", permite_vacio=True)
    if nueva_edad != "":
        usuario["edad"] = nueva_edad
    
    print("Usuario modificado")
    return


       
def listar_usuarios(agenda):

    if len(agenda) == 0:
        print("No hay agenda")
        return

    print("\n--- LISTA DE AGENDA ---")

    for usuario in agenda:

        print(f"\nID: {usuario['id']}")
        print(f"Nombre: {usuario['nombre']}")
        print(f"Email: {usuario['email']}")
        print(f"Edad: {usuario['edad']}")
        
