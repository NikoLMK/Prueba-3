print("Bienvenido a mi programa!!")             #Le damos la bienvenida al usuario
nombre=str(input("Ingrese el nombre del archivo que desea leer: "))      #Aqui le pedimos al usuario que nos ingrese el nombre del archivo que desea abrir.
archivo = open(nombre+'.txt', 'r')          #Con este comando le pedimos que abra el archivo de texto 
contenido = archivo.read()                  #Con este comando le estamos pidiendo al programa que lea el archivo de texto
contadorespacios = contenido.count(' ')     #Con este comando le pedimos que cuente los espacios
print(contenido)                            #Con este print pedimos que nos imprima el texto del archivo
contador_letras = sum(c.isalpha() for c in contenido)  #Con este comando contamos las letras del archivo de texto  #Este comando lo que hace es que "c" es cada caracter del texto, y se van generando todos los caracteres del archivo uno por uno, luego con sum se toman todos los caracteres y se suman
nombre_archivo_nuevo = f"{nombre}_resumen.txt"   #Aqui le damos un nombre a nuestro nuevo archivo, basado en el nombre anterior
archivo_nuevo = open(nombre_archivo_nuevo, 'w')  #Con este comando abrimos un nuevo archivo de texto 
archivo_nuevo.write(f"La cantidad de letras es {contador_letras}\n")  #Con este comando le pedimos al programa que escriba en el archivo nuevo
archivo_nuevo.write(f"La cantidad de espacios es {contadorespacios}\n")  #Lo mismo
archivo_nuevo.close()  #Con este comando cerramos el archivo nuevo 

print(f"Se ha creado y escrito en el archivo '{nombre_archivo_nuevo}' la cantidad de letras y espacios, Gracias por utilizar mi codigo!!.") #Nos despedimos del usuario