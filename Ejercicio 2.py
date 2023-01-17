# Escribir una función que lea dos ficheros csv con una lista larga de datos de personas (50 personas y 1000 personas)
# y llame a dos funciones que pongan su nombre en formato capitalizado y calculen la letra de DNI correspondiente.
# Realiza la comprobación de rendimiento con la librería cProfile y muestra los datos.
# Describe que indica cada dato que nos proporciona cProfile.
import cProfile
def check_DGT(ruta):
   file = open(ruta, 'r', encoding="utf-8")
   lineas = file.readlines()
   lista = []
   for linea in lineas:
       lista1 = []
       datos = linea.split(",")
       nombre = check_username(datos[0])
       nif =  check_nif(datos[1])
       lista1.append(nombre)
       lista1.append(nif)
       lista.append(lista1)
   print(lista)
   return

def check_nif(user_nif):
   """
   Función para corregir mediante la forma matemática la letra del NIF
   :param user_nif: NIF del usuario
   :return: Devuelve el mismo número dl NIF pero con la letra correcta
   """
   nif_numero = user_nif[0:8]
   letra_correcta = nif_dict[(str(int(nif_numero) % 23))]
   return nif_numero + letra_correcta

nif_dict = {'0': "T", '1': "R", '2': "W", '3': "A", '4': "G",
               '5': "M", '6':"Y", '7':"F", '8': "P",
               '9': "D", '10': "X", '11': "B", '12': "N",
               '13':"J", '14': "Z", '15': "S", '16': "Q",
               '17': "V", '18': "H", '19': "L", '20': "C",
               '21': "K", '22': "E"}


def check_username(user_name):
   """
   Función para corregir los nombres y apellidos y ponerlos en formato capitalizado
   :param user_name: Nombre y apellido en formato no capitalizado
   :return: Devuelve el nombre en formato capitalizado
   """
   return user_name.title()
check_DGT('C:\datos\Documents/50.csv')
cProfile.run("check_DGT('C:\datos\Documents/50.csv')")