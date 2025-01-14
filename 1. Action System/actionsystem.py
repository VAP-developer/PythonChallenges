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


