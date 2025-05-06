import os

# Función para determinar el rango según el número de boletos comprados
def determinar_rango(boletos):
    if boletos <= 10:
        return "Fan"
    elif 11 <= boletos <= 20:
        return "Fanático"
    else:
        return "Superfanático"

# Función para cargar usuarios desde el archivo
def cargar_usuarios():
    usuarios = {}
    if os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "r") as file:
            for linea in file:
                username, password, boletos, peliculas = linea.strip().split(",")
                historial = eval(peliculas)  # Convertir el string a diccionario
                usuarios[username] = {"password": password, "boletos": int(boletos), "historial": historial}
    return usuarios

# Función para guardar usuarios en el archivo
def guardar_usuarios(usuarios):
    with open("usuarios.txt", "w") as file:
        for username, data in usuarios.items():
            file.write(f"{username},{data['password']},{data['boletos']},{data['historial']}\n")

# Función para mostrar la cartelera
def mostrar_cartelera():
    peliculas = [
        "Avatar: El camino del agua",
        "Spider-Man: A través del Spider-Verso",
        "Oppenheimer",
        "Elementos",
        "John Wick 4"
    ]
    print("\n--- Cartelera ---")
    for i, pelicula in enumerate(peliculas, start=1):
        print(f"{i}. {pelicula}")
    return peliculas

# Programa principal
def main():
    print("Bienvenido a Cinépolis. Es un placer atenderte. ¿En qué puedo ayudarte?")
    
    usuarios = cargar_usuarios()
    
    while True:
        print("\n--- Registro de Usuarios Cinépolis ---")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Ver cartelera")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Registrar nuevo usuario
            username = input("Nombre de usuario: ")
            if username in usuarios:
                print("El usuario ya existe. Intenta con otro nombre.")
                continue
            password = input("Contraseña: ")
            usuarios[username] = {"password": password, "boletos": 0, "historial": {}}
            guardar_usuarios(usuarios)
            print("Usuario registrado con éxito.")

        elif opcion == "2":
            # Iniciar sesión
            username = input("Nombre de usuario: ")
            password = input("Contraseña: ")
            if username in usuarios and usuarios[username]["password"] == password:
                print("Inicio de sesión exitoso.")
                while True:
                    print("\n1. Comprar boletos")
                    print("2. Ver historial de películas")
                    print("3. Salir de sesión")
                    accion = input("Selecciona una acción: ")

                    if accion == "1":
                        peliculas = mostrar_cartelera()
                        boletos_por_pelicula = {}
                        while True:
                            seleccion = input("Selecciona el número de la película (o escribe 'listo' para finalizar): ")
                            if seleccion.lower() == "listo":
                                break
                            if seleccion.isdigit() and 1 <= int(seleccion) <= len(peliculas):
                                pelicula = peliculas[int(seleccion) - 1]
                                boletos = int(input(f"¿Cuántos boletos deseas para '{pelicula}'? "))
                                if pelicula in boletos_por_pelicula:
                                    boletos_por_pelicula[pelicula] += boletos
                                else:
                                    boletos_por_pelicula[pelicula] = boletos
                            else:
                                print("Selección inválida. Intenta nuevamente.")
                        
                        if boletos_por_pelicula:
                            usuarios[username]["historial"].update(boletos_por_pelicula)
                            usuarios[username]["boletos"] += sum(boletos_por_pelicula.values())
                            visitas = len(boletos_por_pelicula)  # Cada película cuenta como una visita
                            print(f"Has agregado {visitas} visitas por estas compras.")
                            rango = determinar_rango(usuarios[username]["boletos"])
                            guardar_usuarios(usuarios)
                            print(f"¡Compra realizada con éxito! Ahora tienes {usuarios[username]['boletos']} boletos.")
                            print(f"Tu rango es: {rango}.")
                        else:
                            print("No se realizó ninguna compra.")
                    
                    elif accion == "2":
                        print("\n--- Historial de Películas ---")
                        if usuarios[username]["historial"]:
                            for pelicula, boletos in usuarios[username]["historial"].items():
                                print(f"{pelicula}: {boletos} boletos")
                        else:
                            print("Aún no has comprado boletos.")
                    
                    elif accion == "3":
                        break
                    
                    else:
                        print("Opción no válida. Por favor, intenta de nuevo.")
            else:
                print("Usuario o contraseña incorrectos.")

        elif opcion == "3":
            # Mostrar cartelera
            mostrar_cartelera()

        elif opcion == "4":
            # Salir del programa
            print("¡Gracias por usar el registro de usuarios Cinépolis! Hasta pronto.")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()