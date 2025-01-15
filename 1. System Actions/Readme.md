# Program: System Actions

In this program, we are going to make a script that it display the system information and we are going to choose a system option.

# Index

    1. Library os
    2. Library platform
    3. Library psutil
    4. Main

# Library os

Esta libreria la necesitamos para interactuar con el sistema operativo.
Un primer paso para esta libreria es saber cual es nuestro sistema operativo

We need this library to interact with the operating system.
we use os.name to know what our operating sistem is.
Late we will use os.system(command) to execute systems commands.
 
```python
import os

print(os.name)
```

# Library platform

We use this library to extract system information.
We will use platform to know the name, version and other information of our system.

```python
import platform

print("Name OS: ", platform.system())
print("Version OS: ", platform.release())
```
# Library psutil

We can extract information about system processes and resources.
We use the function virtual_memory() to extract memory information and we will extract the total memory (.total), used memory (.used) and available memory (.available).

```python
import psutil

print(f"Memory Total: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")
print(f"Memory Used: {psutil.virtual_memory().used / (1024 ** 3):.2f} GB")
print(f"Memory Available: {psutil.virtual_memory().available / (1024 ** 3):.2f} GB\n")
```

# Main

The program is going to show system information and after we can choose a system option:
    1. Shutdown
    2. Reboot
    3. Log out
    4. Exit

For this, we will create two auxiliary functions. Thi first function will show the system information and the second function will take care of the system options.

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
