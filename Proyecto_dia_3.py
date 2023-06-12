# 1. Pedir al usuario que ingrese un texto
# 2. Pedir al usuario que ingrese 3 letras
# El programa va a hacer
# 1. cuantas veces aparece cada letra (almacena las letras en una lista) metodo que cuente "len"? pasar texto y letras a minusculas
# 2. cuantas palabras hay en total (usa metodos para transformarlo en lista y para calcular su longitud)
# 3. primera y ultima letra del texto indentacion?
# 4. devuelve palabras en orden inverso
# 5. pregunta si aparece python ( usa bools para verificar si se encuentra, y un diccionario para asociar el booleano con un string para mostrar al usuario

texto = input("Ingresa un texto: ")
letras = []

texto = texto.lower()

letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())

print("\n")
print("CANTIDAD DE LETRAS")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])
print(f"Hemos encontrado la letra '{letras[0]}' repetida  {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida:  {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida:  {cantidad_letras3} veces")

print("\n")
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")

print("\n")
print("LETRAS DE INICIO Y DE FIN")
letra_inicio = texto[0]
letra_fin = texto[-1]
print(f"la letra de inicio es '{letra_inicio}' y la letra final es '{letra_fin}'")

print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos tu texto al revés va a decir: '{texto_invertido}'")

print("\n")
print("BUSCANDO LA PALABRA PYHTON")
buscar_python = 'python' in texto
dic = {True:"sí", False: "no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")