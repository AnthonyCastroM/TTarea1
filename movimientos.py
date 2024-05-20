from os import system
import time
import Conexion as conn
db = conn.DB()

# Funciones CRUD para la tabla movimientos
#Funcion Crear
def create_movimiento():
    id_producto = input("Ingrese el ID del producto: ")
    accion = input("Ingrese la acción (añadir/retirar): ")
    sql = "INSERT INTO movimientos (id_producto, accion) VALUES (?,?)"
    parametros = (id_producto, accion)
    db.ejecutar_consulta(sql, parametros)
    print("Movimiento agregado con éxito")

#Funcion Buscar TODOS
def read_movimiento():
    sql = "SELECT * FROM movimientos"
    result = db.ejecutar_consulta(sql)
    for movimiento in result:
        print(f"ID Movimiento: {movimiento[0]}, ID Producto: {movimiento[1]}, Acción: {movimiento[2]}")

#Funcion Actualizar
def update_movimiento():
    id_movimiento = input("Ingrese el ID del movimiento a modificar: ")
    id_producto = input("Actualice el ID del producto: ")
    accion = input("Actualice la acción (añadir/retirar): ")
    sql = "UPDATE movimientos SET id_producto=?, accion=? WHERE id=?"
    parametros = (id_producto, accion, id_movimiento)
    db.ejecutar_consulta(sql, parametros)
    print("Movimiento actualizado con éxito")

#Funcion Eliminar
def delete_movimiento():
    id_movimiento = input("Ingrese el ID del movimiento a eliminar: ")
    sql = "DELETE FROM movimientos WHERE id=?"
    parametros = (id_movimiento,)
    db.ejecutar_consulta(sql, parametros)
    print("Movimiento eliminado con éxito")

#Funcion buscar especifico
def search_movimiento():
    accion = input("Ingrese la acción a buscar (añadir/retirar): ")
    sql = "SELECT * FROM movimientos WHERE accion LIKE ?"
    parametros = ('%{}%'.format(accion),)
    result = db.ejecutar_consulta(sql, parametros)
    for movimiento in result:
        print(f"ID Movimiento: {movimiento[0]}, ID Producto: {movimiento[1]}, Acción: {movimiento[2]}")

