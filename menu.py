from os import system
import time
import producto
import ubicacion
import movimientos


def main_menu():
    while True:
        print("*********************************")
        print("      \tGestión de Inventario        ") 
        print("*********************************")
        print("\t[1] Menu Producto.")
        print("\t[2] Menu Ubicaciones.")
        print("\t[3] Menu Movimientos.")
        print("\t[4] Salir.")
        print("*********************************")
        try:
            opcion = int(input("Seleccione una Opción: "))
            if opcion == 1:
                producto_menu()
            elif opcion == 2:
                ubicacion_menu()
            elif opcion == 3:
                movimiento_menu()
            elif opcion == 4:
                break
            time.sleep(1)
            system("clear")
        except Exception as e:
            print("Error: ", str(e))
            print("Seleccione una opción correcta")
            time.sleep(1)
            system("clear")



def producto_menu():
    while True:
        print("*********************************")
        print("      \tGestión de Inventario        ") 
        print("*********************************")
        print("\t[1] Agregar Producto.")
        print("\t[2] Consultar Productos.")
        print("\t[3] Actualizar Producto.")
        print("\t[4] Eliminar Producto.")
        print("\t[5] Buscar Producto.")
        print("\t[6] Salir del sistema.")
        print("*********************************")
        try:
            opcion = int(input("Seleccione una Opción: "))
            if opcion == 1:
                producto.create_producto()
            elif opcion == 2:
                producto.read_producto()
            elif opcion == 3:
                producto.update_producto()
            elif opcion == 4:
                producto.delete_producto()
            elif opcion == 5:
                producto.search_producto()
            elif opcion == 6:
                break
            time.sleep(1)
            system("clear")
        except Exception as e:
            print("Error: ", str(e))
            print("Seleccione una opción correcta")
            time.sleep(1)
            system("clear")



def ubicacion_menu():
    while True:
        print("*********************************")
        print("       \tGestión de Ubicaciones       ") 
        print("*********************************")
        print("\t[1] Agregar Ubicación.")
        print("\t[2] Consultar Ubicaciones.")
        print("\t[3] Actualizar Ubicación.")
        print("\t[4] Eliminar Ubicación.")
        print("\t[5] Buscar Ubicación.")
        print("\t[6] Salir del menú de ubicaciones.")
        print("*********************************")
        try:
            opcion = int(input("Seleccione una Opción: "))
            if opcion == 1:
                ubicacion.create_ubicacion()
            elif opcion == 2:
                ubicacion.read_ubicacion()
            elif opcion == 3:
                ubicacion.update_ubicacion()
            elif opcion == 4:
                ubicacion.delete_ubicacion()
            elif opcion == 5:
                ubicacion.search_ubicacion()
            elif opcion == 6:
                break
            time.sleep(1)
            system("clear")
        except Exception as e:
            print("Error: ", str(e))
            print("Seleccione una opción correcta")
            time.sleep(1)
            system("clear")


def movimiento_menu():
    while True:
        print("*********************************")
        print("       \tGestión de Movimientos       ") 
        print("*********************************")
        print("\t[1] Agregar Movimiento.")
        print("\t[2] Consultar Movimientos.")
        print("\t[3] Actualizar Movimiento.")
        print("\t[4] Eliminar Movimiento.")
        print("\t[5] Buscar Movimiento.")
        print("\t[6] Salir del menú de movimientos.")
        print("*********************************")
        try:
            opcion = int(input("Seleccione una Opción: "))
            if opcion == 1:
                movimientos.create_movimiento()
            elif opcion == 2:
                movimientos.read_movimiento()
            elif opcion == 3:
                movimientos.update_movimiento()
            elif opcion == 4:
                movimientos.delete_movimiento()
            elif opcion == 5:
                movimientos.search_movimiento()
            elif opcion == 6:
                break
            time.sleep(1)
            system("clear")
        except Exception as e:
            print("Error: ", str(e))
            print("Seleccione una opción correcta")
            time.sleep(1)
            system("clear")

if __name__ == "__main__":
    main_menu()