#!/usr/bin/env python
# coding: utf-8

# Ejercicio 1: Crear un programa que imprima el mensaje “hello world!” por pantalla.

# In[1]:


'''Imprime un dato puro.
No es incorrecto pero el dato no queda guardado en espacio de memoria. Además, si tiene que sufrir una modificación 
a través del código, voy a tener que modificarlo uno por uno. Alojando el dato en una variable (como en el ejercicio 2), 
esto no pasa.'''

print('"hello world!"')


# Ejercicio 2: Crear un programa que almacene el mensaje “hello world!” en una variable y luego lo imprima por pantalla.
# 

# In[2]:


# es mejor porque ya le di el lugar a mi dato en una variable. Lo que manipulo a futuro es la variable y no el dato

mensaje = '"hello world!"'
print(mensaje)


# Ejercicio 3: Crear un programa que pida al usuario nombre y edad e imprima dichos datos en renglones distintos.
# 

# In[2]:


nombre = input('Ingrese su nombre: ') #se deja espacio para que no se pegue el cursor
edad = input('Ingrese su edad: ') # en este caso no es necesario convertirlo en int

''' Como el programa solo pide que imprimamos la edad, o sea que no va a ser utilizada como un numero, no es necesario
convertirlo en un numero entero int(). Al convertirlo en un int() se consume más memoria y más tiempo de ejecución'''

print(nombre)
print(edad)


# In[3]:


print(nombre); print(edad) # se considera mala práctica, se trata de evitar porque puede confundir

'''Puede generar que se rompa el programa.'''


# In[4]:


print(f'''{nombre}
{edad}''')


# In[5]:


print(f'{nombre}\n{edad}')


# Ejercicio 4: Crear un programa que pregunte el nombre del usuario y un número
# entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces
# como el número introducido

# In[6]:


nombre = input('¿Cuál es su nombre? ')
numero = int(input('Ingrese un número. ')) # en este caso si o si se convierte en entero

for i in range (numero):
    print(nombre)


# In[7]:


print(f'{nombre}\n' * numero)


# Ejercicio 5: Crear un programa que pregunte el nombre del usuario y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras. (siempre que aparezca entre mayor y menos, ahi va una variable)

# In[8]:


nombre = input('Coloque su nombre: ')
n = 0 # se inicia en cero porque es un contador y porque es el neutral de la suma

for letra in nombre:
    n += 1
print(f'{nombre} tiene {n} letras.')


# In[9]:


# mejor forma de resolver este ejercicio

nombre = input('Coloque su nombre: ')
n = len(nombre) # len cuenta la cantidad de objetos iterables

print(f'{nombre} tiene {n} letras.')


# Ejercicio 6: Crear un programa que realice la siguiente operación aritmética [(3+2)/2*5]2. Mostrar el resultado por pantalla.

# In[10]:


# sigue la lógica PEMDAS como todos los programas de programación

''' primero va a ser la suma, despues va a dividir por el 2. Despues al resultado lo multiplica por 5. 
Y finalmente lo potencia por 2. Hay diferencias si uno encerrara el 2*5 entre parentesis'''

resultado = ((3+2)/2*5)**2

print(resultado)


# Ejercicio 7: Crear un programa que pida al usuario dos números enteros y muestre por pantalla la división de n en m da un cociente c y un resto r donde n y m son los números introducidos por el usuario, y c y r son el cociente y el resto de la
# división entera respectivamente.

# In[11]:


n = int(input('Ingrese un número.'))
m = int(input('Ingrese un número.'))

print(n // m)
print(n % m)


# In[12]:


n = int(input('Ingrese un número.'))
m = int(input('Ingrese un número.'))
c, r = n // m , n % m

print(f'El cociente es {c} y el resto es {r}.')


# Ejercicio 8: Crear un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
# 

# In[14]:


capital = float(input('Ingrese el capital a invertir: '))
interes_anual = float(input('Ingrese el interés anual: '))
anios = int(input('Ingrese la cantidad de años a invertir: '))

'''El if va a actuar si el usuario expresa el interes anual como un numero flotante. El else actua si lo expresa en forma de
porcentaje'''

if 0 < interes_anual <= 1:
    capital_final = capital + capital * interes_anual * anios
else:
    interes_anual = interes_anual / 100
    capital_final = capital + capital * interes_anual * anios

print(capital_final)


# In[15]:


#otra forma con menos lineas de código

if interes_anual > 1:
    interes_anual = interes_anual / 100
capital_final = capital + capital * interes_anual * anios
print(capital_final)


# Ejercicio 9: Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por el peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán
# en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Crear un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado. Mostrar el resultado por pantalla.

# In[17]:



cant_p = int(input('Ingrese la cantidad de payasos: '))
cant_m = int(input('Ingrese la cantidad de muñecas: '))
peso_p = 112 #gramos
peso_m = 75 #gramos

peso_pqt = cant_p * peso_p + cant_m * peso_m

if peso_pqt < 1000:
    print(f'El peso del paquete es de {peso_pqt} gramos.')
else:
    peso_pqt /= 1000
    print(f'El peso del paquete es de {peso_pqt} kilos.')


# Ejercicio 10: Crear un programa que pida al usuario su edad y muestra por pantalla si es mayor de edad o no, siendo 18 años la mayoría de edad.

# In[18]:


edad = int(input('Ingrese su edad: '))

if edad >= 18:
    print('El usuario es mayor de edad.')
else:
    print('El usuario no es mayor de edad.')


# In[21]:


if 0 < edad < 18:
    print('El usuario no es menor de edad.')
elif edad >= 18:
    print('El usuario es mayor de edad.')
else:
    print('El usuario no ha ingresado una edad correcta.')


# Ejercicio 11: Crear un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable.

# In[22]:


contrasenia = 'contraseña'
usuario = input('Ingrese su contraseña: ')

if contrasenia == usuario:
    print('Las contraseñas coinciden.')
else:
    print('Las contraseñas no coinciden.')


# In[2]:


password = 'password'
user = input('Password: ')

if password == user:
	print()
else:
    print('The passwords do not match')


# In[23]:


# haciendo lo mismo con while

contrasenia = 'contraseña'
usuario = input('Ingrese su contraseña: ')

while True:
    if contrasenia == usuario:
        print('Las contraseñas coinciden.')
        break
    else:
        print('Las contraseñas no coinciden.')
        usuario = input('Ingrese su contraseña: ')


# Ejercicio 12: Crear un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero, el programa debe devolver un mensaje indicando que no se puede dividir por 0.

# In[24]:


num = int(input('Ingrese un número: '))
num_2 = int(input('Ingrese otro número: '))

if num_2 == 0:
    print('No se puede dividir por 0.')
else:
    division = num / num_2
    print(division)


# In[25]:


while True:
    if num_2 != 0:
        division = num / num_2
        print(division)
        break
    else:
        print('No se puede dividir por 0.')
        num_2 = int(input('Ingrese otro número: '))


# Ejercicio 13: Crear un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
# 

# In[26]:


'''tipico challenge es que te pidan recorrer un iterable y saber cuantos numeros son pares o impares. Para eso se usa el for, 
y este truco para saber si un numero es par o impar'''

numero = int(input('Ingrese un numero entero: '))

if numero % 2 == 0:
    print('Este número es par.')
else: 
    print('Este número es impar.')


# In[13]:


number = int(input('Enter a number: '))

if number % 2 == 0:
	print(f'{number} is even')
else:
	print(f'{number} is odd')


# Ejercicio 14: En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir
# los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel
# es de 100000 multiplicada por la puntuación del nivel.Crear un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
# 
# Inaceptable 0.0
# Aceptable 0.4
# Meritorio 0.6 o más

# In[27]:


punt_us = float(input('Indicar la puntuación del usuario: '))
inaceptable = 0.0
aceptable = 0.4
meritorio = 0.6
bonif = 100000

if punt_us == inaceptable:
    bonif *= punt_us # bonif = bonif * punt_us
    print(f'Su rendimiento es inaceptable, recibirá {bonif} pesos.')
elif punt_us == aceptable:
    bonif *= punt_us
    print(f'Su rendimiento es aceptable, recibirá {bonif} pesos.')
elif punt_us >= meritorio:
    bonif *= punt_us
    print(f'Su rendimiento es meritorio, recibirá {bonif} pesos.')
else:
    print('No ha ingresado una puntuación correcta')


# Ejercicio 15: Crear un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 500 y si es mayor de 18 años, 1000.

# In[28]:


edad_cliente = int(input('Edad: '))

if 0 < edad_cliente < 4:
    print('Entra gratis, no abona entrada.')
elif 4 <= edad_cliente < 18:
    print('Debe abonar 500.')
elif edad_cliente >= 18:
    print('Debe abonar 1000.')
else:
    print('No ingresó una edad correcta')


# Ejercicio 16: Crear un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
# 

# In[29]:


edad_usuario = int(input('Ingrese su edad: '))

for i in range(1, edad_usuario + 1):
    print(f'Ha cumplido {i}')


# Ejercicio 17: Crear un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

# In[30]:


'''Cuando hay for anidado, no se pasa al for general hasta que no se terminen las interacciones del for anidado'''


for i in range(1, 11): # 1, 10
    print(f'Tabla de {i}')
    for j in range(10):
        print(f'{i} * {j} = {i*j}')
    print()


# Ejercicio 18: Crear un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

# In[31]:



palabra = input('Ingrese una palabra: ')

for letra in palabra[::-1]:
    print(letra)


# In[32]:


for letra in reversed(palabra):
    print(letra)


# Ejercicio 19: Crear un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
# 

# In[34]:


frase = input('Ingrese una frase: ')
letra = input('Ingrese una letra: ')

print(f'La letra {letra} aparece {frase.count(letra)} en la frase.')


# In[35]:


frase = input('Ingrese una frase: ')
letra = input('Ingrese una letra: ')

cant_veces = 0 #contador

for caracter in frase:
    if caracter == letra:
        cant_veces += 1
print(f'La letra {letra} aparece {cant_veces} en la frase.')


# Ejercicio 20: Crear un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
# 

# In[36]:


#se suele tomar en challenges

palabra = input('Ingrese una palabra: ')

while palabra != 'salir':
    print(palabra)
    palabra = input('Ingrese una palabra o escriba "salir" para terminar: ')
    


# In[37]:


while True:
    palabra = input('Ingrese una palabra o escriba "salir" para terminar: ')
    if palabra != 'salir':
        print(palabra)
    else:
        break
        
    


# Ejercicio 21: Crear un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y muestre por pantalla el mensaje “Yo estudio asignatura”, donde asignatura es cada una de las asignaturas de la lista.
# 

# In[38]:


lista_asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']

for materia in lista_asignaturas:
    print(f'Yo estudio {materia}.')


# Ejercicio 22: Crear un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.Fruta
# Banana: 80-
# Manzana:100-
# Pera: 120-
# Naranja: 150
# 

# In[41]:


frutas = {
    'Banana': 80,
    'Manzana': 100,
    'Pera': 120,
    'Naranja': 150,
}

fruta = input('Ingrese una fruta: ').capitalize()  #para que no importe si el usuario escribe en minuscula o mayuscula
kilos = float(input('Ingrese la cantidad de kilos: '))

if fruta in frutas:
    precio = frutas[fruta] * kilos
    print(f'Debe pagar {precio} pesos.')

else:
    print('La fruta no está en el diccionario.')

# volver a repasar diccionarios



    


# Ejercicio 23:Crear un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato asignatura tiene créditos créditos, donde asignatura es cada una de las asignaturas del curso, y créditos son sus créditos. Al final debe mostrar también el número total de créditos del curso.

# In[43]:


materias = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_cred = 0

for i, k in materias.items():
    print(f'{i} tiene {k} creditos.')
    total_cred += k
print(f'El total de créditos es {total_cred}.') # tiene que estar afuera del for para que no se repita 


# In[ ]:




