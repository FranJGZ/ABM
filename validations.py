from email_validator import validate_email, EmailNotValidError


    
def get_dni(message, allow_empty=False):
    while True:
        user_input = input(message).strip()

        if user_input == "" and allow_empty:
            return ""

        if user_input.isdigit() and 7 <= len(user_input) <= 8:
            return user_input

        print("Error: El DNI debe tener 7 u 8 números, sin puntos ni letras.")
            
def get_email(message, allow_empty=False):
    while True:
        user_input = input(message).strip()
        if user_input == "" and allow_empty:
            return ""

        try:
            validate_email(user_input, check_deliverability=False)
            return user_input

        except EmailNotValidError:
            print("Email inválido. Intente nuevamente.")
        

def get_unique_email(message, user_list):
    while True:
        email = get_email(message)
        
        is_duplicate = False
        for user in user_list:
            if user["email"] == email:
                is_duplicate = True

        if is_duplicate:
            print("Ese email ya está registrado. Por favor, intente con otro.")
        else:
            return email 
def get_confirmation(message):
    while True:
        answer = input(message).strip().lower()
        if answer == 's':
            return True
        elif answer == 'n':
            return False
        print("Error: Por favor ingrese 's' para confirmar o 'n' para cancelar.")

def get_name(message, allow_empty=False):
    
    while True:
        user_input = input(message).strip()
        
        if user_input == "" and allow_empty:
            return ""
            
        if user_input.replace(" ", "").isalpha():
            return user_input
            
        print("Error: El nombre debe contener solo letras y no puede estar vacío.")
        
def get_user_by_id(message, user_list):
    
    while True:
        user_input = input(message).strip()
        
        try:
            id_user = int(user_input)
            for user in user_list:
                if user["id"] == id_user:
                    return user 
            print("Error: El ID ingresado no existe en la lista de usuarios. Intente de nuevo.")
            
        except ValueError:
            print("Error: ID inválido. Debe ingresar un número entero.")
            
def print_user_card(user):
    print("\n" + "="*40)
    print(f"ID:    {user['id']}")
    print(f"Nombre:  {user['name']}")
    print(f"DNI:   {user['dni']}")
    print(f"Email: {user['email']}")
    print("="*40 + "\n")