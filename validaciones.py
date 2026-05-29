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

    
        if entrada == "" and permite_vacio:
            return "" 
            
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

        if entrada == "" and permite_vacio:
            return ""

        if validar_email(entrada):
            return entrada
            
        print("Email inválido. Intente nuevamente.")

def pedir_email_unico(mensaje, agenda):
  
    while True:
       
        email = pedir_email(mensaje)
        
        
        es_duplicado = False
        for usuario in agenda:
            if usuario["email"] == email:
                es_duplicado = True
                break  
        
     
        if es_duplicado:
            print("Ese email ya está registrado. Por favor, intente con otro.")
        else:
            return email 
        
def pedir_confirmacion(mensaje):
   
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta == 's':
            return True
        elif respuesta == 'n':
            return False
        print("Error: Por favor ingrese 's' para confirmar o 'n' para cancelar.")

def pedir_nombre(mensaje, permite_vacio=False):
    
    while True:
        entrada = input(mensaje).strip()
        
        if entrada == "" and permite_vacio:
            return ""
            
        if entrada != "":
            return entrada
            
        print("Error: El nombre no puede estar vacío.")
        
def pedir_usuario_por_id(mensaje, agenda):
    
    while True:
        entrada = input(mensaje).strip()
        try:
            id_usuario = int(entrada)
            
           
            for usuario in agenda:
                if usuario["id"] == id_usuario:
                    return usuario 
          
            print("Error: El ID ingresado no existe en la agenda. Intente de nuevo.")
            
        except ValueError:
            print("Error: ID inválido. Debe ingresar un número entero.")
            
