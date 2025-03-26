#Primer Parte: Aquí importamos los comandos necesarios para poder realizar nuestro objetivo
import random as r
import pandas as pd
#Segunda Parte: Aquí tenemos nuestras listas correspondientes que usaremos para usar las funciones de random
abecedario=[ 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z']
papelerias = ['Xochimilco', 'Cuemanco', 'Coapa', 'Milpa Alta', 'CU', 'Zócalo',
              'Narvarte', 'Santa Fé', 'Polanco', 'Centro']
lineas = ['Cuadernos', 'Libretas', 'Lápices', 'Plumones', 'Borradores', 'Sacapuntas',
          'Laptops', 'Tablets', 'Mochilas', 'Bolsas', 'Cajas', 'Pegamento', 'Tijeras',
          'Monitores', 'Teclados', 'Mouse', 'Audífonos', 'Cables', 'Cargadores', 'Baterías',
          'Pc', 'Uniformes', 'Pinturas', 'Pinceles', 'Papel', 'Cartulinas']

#fecha = "16/03/2025"
#sucursal = r.choice(papelerias)
#producto = r.choice(lineas)
#clave_producto = r.choice(abecedario) + r.choice(abecedario) + r.choice(abecedario) + "-" + str(r.randint(1,9)) + str(r.randint(1,9)) + str(r.randint(1,9))
#precio = r.random() * r.randint(100,5000) 
#cantidad_vendida = r.randint(1,20)
#total_ticket = precio * cantidad_vendida 
#print(f"Fecha: {fecha}")
#print(f"Sucursal: {sucursal}")
#print(f"Producto: {producto}")
#print(f"Clave de Producto: {clave_producto}")
#print(f"Precio: {precio}")
#print(f"Cantidad Vendida: {cantidad_vendida})

#Tercera Parte: Definimos nuevas listas que llenaremos más abajo
fechas = []
sucursales = []
productos = []
claves_producto = []
precios = []
cantidades_vendidas = []
totales_ticket = []

#Cuarta Parte: Usamos el ciclo for para llenar las listas que teníamos arriba
for i in range (1,1001):
 #Información a trabajar.
 fecha = "16/03/2025"
 sucursal = r.choice(papelerias)
 producto = r.choice(lineas)
 clave_producto = r.choice(abecedario) + r.choice(abecedario) + r.choice(abecedario) + "-" + str(r.randint(1,9)) + str(r.randint(1,9)) + str(r.randint(1,9))
 precio = r.random() * r.randint(100,5000) 
 cantidad_vendida = r.randint(1,20)
 total_ticket = precio * cantidad_vendida

 
 #Quinte Parte: Agregamos a listas usando .append
 fechas.append(fecha)
 sucursales.append(sucursal)
 productos.append(producto)
 claves_producto.append(clave_producto)
 precios.append(precio)
 cantidades_vendidas.append(cantidad_vendida)
 totales_ticket.append(total_ticket)

#Sexta Parte: Definimos nuestro diccionario para después usar la funcion DataFrame
dc_1 = {
    "Fecha": fechas,
    "Sucursal" : sucursales,
    "Producto" : productos,
    "Clave_producto" : claves_producto, 
    "Precio": precios,
    "Cantidad_vendida" : cantidades_vendidas,
    "Total" : totales_ticket    
} 
df_ventas = pd.DataFrame(dc_1)
print(df_ventas)

