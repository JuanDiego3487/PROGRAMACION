def menu():
    while True:
        try:
            print("\nNOMINA ACME" )
            print("\nMENU" )
            print("1. Agregar empleado ")
            print("2. Modificar empleado ")
            print("3. Buscar empleado  ")
            print("4. Eliminar empleado  ")
            print("5. Listar empleados  ")
            print("6. Listar nómina de un empleado ")
            print("7. Listar nómina de todos los empleados  ")
            print("8. Salir ")
            op = int(input(">>> Opción (1-8)? "))
            if op < 1 or op > 8:
                print("Opción no válida. Escoja de 1 a 8.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 8.")
            input("Presione cualquier tecla para continuar...")

   