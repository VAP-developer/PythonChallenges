# Program: System Actions

En este programa vamos a crear un script que muestre la información del sistema y vamos a elegir una acción del sistema

# Indice

    1. Libreria os
    2. Libreria platform
    3. Libreria psutil
    4. Main

# Libreria os

Esta libreria la necesitamos para interactuar con el sistema operativo.
Un primer paso para esta libreria es saber cual es nuestro sistema operativo
 
```python
import os

print(os.name)
```

Con os.name podemos saber si nuestro sistema operativo es Windows, Unix u otro.

Esta libreria la usaremos con os.system(command) para ejecutar comandos.

# Libreria platform

Esta libreria nos sirve para extraer información de nuestro sistema.
La usaremos para saber el nombre de nuestro sistema operativa y la version entre otros.

```python
import platform

print("Name OS: ", platform.system())
print("Version OS: ", platform.release())
```
# Libreria psutil

Con esta libreria podemos recoger información de procesos y recursos del sistemas.
En el programa la usamos para obtener información de la memeoria con la funcion virtual_memory().
En esta función usaremos los atributos .total, .used y .available

```python
import psutil

print(f"Memory Total: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")
print(f"Memory Used: {psutil.virtual_memory().used / (1024 ** 3):.2f} GB")
print(f"Memory Available: {psutil.virtual_memory().available / (1024 ** 3):.2f} GB\n")
```

# Main

En el programa va a mostrar información del sistema y despues vamos a elegir una opción para apagar, reinicir, cerrar sesión o salir.

Para ello vamos a tener la funcion resumen para mostrar información del sistema y la funcion acción para realizar una de las opciones

La funcion main se va a encargar de ejecutar ambas funciones pidiendo al usuario que elija una opción de las dadas.

```python
import os
import platform as ptf
import psutil as pst

def summary():
    print("OS: ", os.name)
    if os.name == "posix":
        print("You are using Unix")
    elif os.name == "nt":
        print("You are using Windows")
    else:
        print(os.name)
    print("Name OS: ", ptf.system())
    print("Version OS: ", ptf.release())
    print("Architecture: ", ptf.architecture()[0])
    print("Processor: ", ptf.processor())
    print(f"Memory Total: {pst.virtual_memory().total / (1024 ** 3):.2f} GB")
    print(f"Memory Used: {pst.virtual_memory().used / (1024 ** 3):.2f} GB")
    print(f"Memory Available: {pst.virtual_memory().available / (1024 ** 3):.2f} GB\n")

def action(option):
    if (ptf.system() == "Windows"):
        if option == 1:
            os.system("shutdown /s /t 1")
        elif option == 2:
            os.system("shutdown /r /t 1")
        elif option == 3:
            os.system("shutdown /l")
    elif (ptf.system() in ["Linux", "Darwin"]):
        if option == 1:
            os.system("shutdown now")
        elif option == 2:
            os.system("sudo reboot")
        elif option == 3:
            os.system("logout")
    else:
        print("OS not supported")

def main():
    summary()
    next = 0
    while (next == 0):
        option = int(input("Write a option:\n1. Shutdown\n2. Reboot\n3. Log out\n4. Exit\n > "))
        if option in [1, 2, 3, 4]:
            next = 1
            break
        print("Number wrong\n")
    action(option)

if __name__ == "__main__":
    main()
```
