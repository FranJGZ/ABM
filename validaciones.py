from email_validator import validate_email, EmailNotValidError

def validar_email(email):
    try:
        validate_email(email, check_deliverability=False)
        return True

    except EmailNotValidError:
        return False
    
def pedir_edad(mensaje, permite_vacio=False):
    while True:
        entrada = input(mensaje).strip()

        # Si el usuario da ENTER y nosotros dijimos que "permite_vacio" es True
        if entrada == "" and permite_vacio:
            return "" # Devolvemos un texto vacío, igual que hace el input del nombre
            
        try:
            edad = int(entrada)
            if 0 <= edad <= 120:
                return edad
            print("La edad debe estar entre 0 y 120")
        except ValueError:
            print("Edad inválida")
            
def pedir_email(mensaje, permite_vacio=False):
    while True:
        entrada = input(mensaje).strip()

        # Si presiona ENTER y permitimos vacío (en modificar)
        if entrada == "" and permite_vacio:
            return ""

        # Si escribió algo, usamos tu validador de antes
        if validar_email(entrada):
            return entrada
            
        print("Email inválido. Intente nuevamente.")

def pedir_email_unico(mensaje, agenda):
    """Pide un email, valida su formato y se asegura de que no esté repetido."""
    while True:
        # 1. Usamos tu función base para pedir y validar el formato (el @ y el .com)
        email = pedir_email(mensaje)
        
        # 2. Hacemos la búsqueda de duplicados directamente aquí
        es_duplicado = False
        for usuario in agenda:
            if usuario["email"] == email:
                es_duplicado = True
                break  # Encontramos uno, dejamos de buscar
        
        # 3. Decidimos qué hacer
        if es_duplicado:
            print("Ese email ya está registrado. Por favor, intente con otro.")
        else:
            return email  # Todo perfecto, devolvemos el email
        
def pedir_confirmacion(mensaje):
    """Hace una pregunta y obliga al usuario a responder 's' o 'n'."""
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta == 's':
            return True
        elif respuesta == 'n':
            return False
        print("Error: Por favor ingrese 's' para confirmar o 'n' para cancelar.")

def pedir_nombre(mensaje, permite_vacio=False):
    """Pide un texto y valida que no esté vacío (a menos que se permita)."""
    while True:
        entrada = input(mensaje).strip()
        
        if entrada == "" and permite_vacio:
            return ""
            
        if entrada != "":
            return entrada
            
        print("Error: El nombre no puede estar vacío.")
        
def pedir_usuario_por_id(mensaje, agenda):
    """Pide un ID, asegura que sea número y que exista en la agenda. 
    Devuelve el diccionario del usuario encontrado."""
    while True:
        entrada = input(mensaje).strip()
        try:
            id_usuario = int(entrada)
            
            # Buscamos al usuario en la agenda
            for usuario in agenda:
                if usuario["id"] == id_usuario:
                    return usuario # ¡Bingo! Devolvemos el usuario completo y cerramos la función
            
            # Si el bucle termina y no encontró el ID:
            print("Error: El ID ingresado no existe en la agenda. Intente de nuevo.")
            
        except ValueError:
            print("Error: ID inválido. Debe ingresar un número entero.")
            
