with open('rockyou.txt', 'r', encoding='latin-1') as file:
    original_passwords = file.readlines()

modified_passwords = []

for password in original_passwords:
    password = password.strip()  # Elimina espacios en blanco al principio y al final

    # Verifica si la contraseña no está vacía y si no comienza con un número
    if password and not password[0].isdigit():
        # Convierte la primera letra en mayúscula y agrega '0' al final
        modified_password = password[0].upper() + password[1:] + '0'
        modified_passwords.append(modified_password)

with open('rockyou_mod.dic', 'w') as file:
    for password in modified_passwords:
        file.write(password + '\n')

print(f'El diccionario modificado tiene {len(modified_passwords)} contraseñas.')
