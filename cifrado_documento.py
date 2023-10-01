import os
from cryptography.fernet import Fernet

def generar_clave():
    return Fernet.generate_key()

def cifrar_documento(nombre_archivo, clave):
    fernet = Fernet(clave)
    nombre_archivo_cifrado = nombre_archivo + '.cifrado'
    with open(nombre_archivo, 'rb') as archivo_original:
        datos = archivo_original.read()        
    with open(nombre_archivo_cifrado, 'wb') as archivo_cifrado:        
        archivo_cifrado.write(datos)
    os.remove(nombre_archivo)
    print(f"Documento '{nombre_archivo}' cifrado con éxito.")

def descifrar_documento(nombre_archivo_cifrado, clave):
    fernet = Fernet(clave)
    nombre_archivo_original = nombre_archivo_cifrado.rstrip('.cifrado')
    with open(nombre_archivo_cifrado, 'rb') as archivo_cifrado:
        datos = archivo_cifrado.read()        
    with open(nombre_archivo_original, 'wb') as archivo_original:
        archivo_original.write(datos)
    os.remove(nombre_archivo_cifrado)
    print(f"Documento '{nombre_archivo_original}' descifrado con éxito.")

# Nombre del documento que deseas cifrar
documento_a_cifrar = 'documento.txt'

# Generar una clave (deberías almacenarla de manera segura)
clave = generar_clave()

#Cifrar el documento
# cifrar_documento(documento_a_cifrar, clave)

# Para descifrar el documento, usa:
descifrar_documento('documento.txt.cifrado', clave)