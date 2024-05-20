from os import system
import time
import Conexion as conn
db = conn.DB()


# Funciones CRUD para la tabla ubicaciones
#Funcion Crear
def create_ubicacion():
    bodega = input("Ingrese la bodega: ")
    pasillo = input("Ingrese el pasillo: ")
    estante = input("Ingrese el estante: ")
    sql = "INSERT INTO ubicaciones (bodega, pasillo, estante) VALUES (?,?,?)"
    parametros = (bodega, pasillo, estante)
    db.ejecutar_consulta(sql, parametros)
    print("Ubicación agregada con éxito")

#Funcion Buscar TODOS
def read_ubicacion():
    sql = "SELECT * FROM ubicaciones"
    result = db.ejecutar_consulta(sql)
    for ubicacion in result:
        print(f"ID: {ubicacion[0]}, Bodega: {ubicacion[1]}, Pasillo: {ubicacion[2]}, Estante: {ubicacion[3]}")

#Funcion Actualizar
def update_ubicacion():
    id = input("Ingrese el ID de la ubicación a modificar: ")
    bodega = input("Actualice la bodega: ")
    pasillo = input("Actualice el pasillo: ")
    estante = input("Actualice el estante: ")
    sql = "UPDATE ubicaciones SET bodega=?, pasillo=?, estante=? WHERE id=?"
    parametros = (bodega, pasillo, estante, id)
    db.ejecutar_consulta(sql, parametros)
    print("Ubicación actualizada con éxito")

#Funcion Eliminar
def delete_ubicacion():
    id = input("Ingrese el ID de la ubicación a eliminar: ")
    sql = "DELETE FROM ubicaciones WHERE id=?"
    parametros = (id,)
    db.ejecutar_consulta(sql, parametros)
    print("Ubicación eliminada con éxito")

#Funcion buscar especifico
def search_ubicacion():
    bodega = input("Ingrese la bodega a buscar: ")
    sql = "SELECT * FROM ubicaciones WHERE bodega LIKE ?"
    parametros = ('%{}%'.format(bodega),)
    result = db.ejecutar_consulta(sql, parametros)
    for ubicacion in result:
        print(f"ID: {ubicacion[0]}, Bodega: {ubicacion[1]}, Pasillo: {ubicacion[2]}, Estante: {ubicacion[3]}")

