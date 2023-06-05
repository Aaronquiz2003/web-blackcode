
# Definir una clase para representar a los usuarios
class Usuario:
    def __init__(self, nombre, cedula, edad, email, genero, ocupacion):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.email = email
        self.genero = genero
        self.ocupacion = ocupacion

# Crear una lista para almacenar los usuarios
usuarios = []

# Función para agregar un nuevo usuario
def agregar_usuario():
    nombre = input("Nombre: ")
    cedula = input("Cédula: ")
    edad = input("Edad: ")
    email = input("Email: ")
    genero = input("Género: ")
    ocupacion = input("Ocupación: ")
    usuario = Usuario(nombre, cedula, edad, email, genero, ocupacion)
    usuarios.append(usuario)
    print("Usuario agregado exitosamente.")

# Función para actualizar los datos de un usuario existente
def actualizar_usuario():
    cedula = input("Ingrese la cédula del usuario que desea actualizar: ")
    for usuario in usuarios:
        if usuario.cedula == cedula:
            nombre = input("Nuevo nombre: ")
            edad = input("Nueva edad: ")
            email = input("Nuevo email: ")
            genero = input("Nuevo género: ")
            ocupacion = input("Nueva ocupación: ")
            usuario.nombre = nombre
            usuario.edad = edad
            usuario.email = email
            usuario.genero = genero
            usuario.ocupacion = ocupacion
            print("Usuario actualizado exitosamente.")
            return
    print("No se encontró ningún usuario con esa cédula.")

# Función para eliminar un usuario
def eliminar_usuario():
    cedula = input("Ingrese la cédula del usuario que desea eliminar: ")
    for usuario in usuarios:
        if usuario.cedula == cedula:
            usuarios.remove(usuario)
            print("Usuario eliminado exitosamente.")
            return
    print("No se encontró ningún usuario con esa cédula.")

# Función principal para interactuar con el programa
def main():
    while True:
        print("\n***** MENU *****")
        print("1. Agregar usuario")
        print("2. Actualizar usuario")
        print("3. Eliminar usuario")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_usuario()
        elif opcion == "2":
            actualizar_usuario()
        elif opcion == "3":
            eliminar_usuario()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Ejecutar el programa
main()



