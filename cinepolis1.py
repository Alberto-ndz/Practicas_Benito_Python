import os

def determinar_rango(visitas):
    if visitas <= 10:
        return "Fan"
    elif 11 <= visitas <= 20:
        return "Fanático"
    else:
        return "Superfanático"

def cargar_usuarios():
    usuarios = {}
    if os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "r") as file:
            for linea in file:
                username, password, visitas = linea.strip().split(",")
                usuarios[username] = {"password": password, "visitas": int(visitas)}
    return usuarios

def guardar_usuarios(usuarios):
    with open("usuarios.txt", "w") as file:
        for username, data in usuarios.items():
            file.write(f"{username},{data['password']},{data['visitas']}\n")

def main():
    usuarios = cargar_usuarios()
    
    while True:
        print("\n--- Registro de Usuarios Cinépolis ---")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            username = input("Nombre de usuario: ")
            if username in usuarios:
                print("El usuario ya existe. Intenta con otro nombre.")
                continue
            password = input("Contraseña: ")
            usuarios[username] = {"password": password, "visitas": 0}
            guardar_usuarios(usuarios)
            print("Usuario registrado con éxito.")

        elif opcion == "2":
            username = input("Nombre de usuario: ")
            password = input("Contraseña: ")
            if username in usuarios and usuarios[username]["password"] == password:
                print("Inicio de sesión exitoso.")
                usuarios[username]["visitas"] += 1
                rango = determinar_rango(usuarios[username]["visitas"])
                guardar_usuarios(usuarios)
                print(f"¡Hola {username}! Actualmente tienes {usuarios[username]['visitas']} visitas.")
                print(f"Tu rango es: {rango}.")
            else:
                print("Usuario o contraseña incorrectos.")

        elif opcion == "3":
            print("¡Gracias por usar el registro de usuarios Cinépolis! Hasta pronto.")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()