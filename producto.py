from os import system
import time
import ubicacion
import Conexion as conn
db = conn.DB()

# CRUD para productos
#Funcion Crear
def create_producto():
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio = input("Ingrese el precio unitario del producto: ")
    cantidad = input("Ingrese la cantidad inicial del producto: ")
    print("Ubicacion producto")
    ubicacion.read_ubicacion()
    # bodega = input("Ingrese la bodega donde se ubica el producto: ")
    # pasillo = input("Ingrese el pasillo del producto: ")
    # estante = input("Ingrese el estante del producto: ")
    sql = "INSERT INTO productos (codigo, nombre, precio, cantidad, bodega, pasillo, estante) VALUES (?,?,?,?,?,?,?)"
    parametros = (codigo, nombre, precio, cantidad)
    db.ejecutar_consulta(sql, parametros)
    print("Producto agregado con éxito")

#Funcion Buscar TODOS
def read_producto():
    sql = "SELECT * FROM productos"
    result = db.ejecutar_consulta(sql)
    for producto in result:
        print("Código: {}, Nombre: {}, Precio: {}, Cantidad: {}".format(producto[0], producto[1], producto[2], producto[3]))

#Funcion Actualizar
def update_producto():
    codigo = input("Ingrese el código del producto a modificar: ")
    nombre = input("Actualice el nombre del producto: ")
    precio = input("Actualice el precio unitario del producto: ")
    cantidad = input("Actualice la cantidad del producto: ")
    sql = "UPDATE productos SET nombre=?, precio=?, cantidad=? WHERE codigo=?"
    parametros = (nombre, precio, cantidad, codigo)
    db.ejecutar_consulta(sql, parametros)
    print("Producto actualizado con éxito")

#Funcion Eliminar
def delete_producto():
    codigo = input("Ingrese el código del producto a eliminar: ")
    sql = "DELETE FROM productos WHERE codigo=?"
    parametros = (codigo,)
    db.ejecutar_consulta(sql, parametros)
    print("Producto eliminado con éxito")

#Funcion buscar especifico
def search_producto():
    nombre = input("Ingrese el nombre del producto a buscar: ")
    sql = "SELECT * FROM productos WHERE nombre LIKE ?"
    parametros = ('%{}%'.format(nombre),)
    result = db.ejecutar_consulta(sql, parametros)
    for producto in result:
        print("Código: {}, Nombre: {}, Precio: {}, Cantidad: {}".format(producto[0], producto[1], producto[2], producto[3]))

