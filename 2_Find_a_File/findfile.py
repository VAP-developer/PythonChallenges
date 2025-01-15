# Encontrar un fichero
# Basico: Nombre y directorio
# Intermedio: Recursivamente
# Avanzado: Patrones (*.txt)
# Creativa: Interfaz grafico

# os.walk -> Recorre directorios recursivamente. Tupla [Dir actual, Subdir, Files]

import os

# Basic search
def search_file(file_name, directory):
    files = os.listdir(directory)
    if file_name in files:
        print("Find!")
    else:
        print("Dont find :(")

def ft_walk(dir):
    # Es una tupla de 3
    result = []
    files = []
    dirs = []
    root = [dir]
    dir_complete = os.listdir(dir) # Lista de archivos en el dir actual
    for d in dir_complete:
        d = os.path.join(dir, d)
        if (os.path.isdir(d)):
            dirs.append(d)
        else:
            files.append(d)
    result.append((root, dirs, files))
    
    for subdir in dirs:
        subdir_result = ft_walk(subdir)
        result.extend(subdir_result)
    return (result)

# ft_walk() -> os.walk()
def recursive_search(file_name, directory):
    for root, dirs, file in ft_walk(directory):
        for name in file:
            if file_name in name:
                print(name)

def main2():
    file = "Readme.md"
    dir = "/Users/vicalons/Documents/PyC"
    recursive_search(file, dir)
    #print(ft_walk(dir)[1])
    #print(ft_walk(dir)[2])

def main():
    file = str(input("Name file: "))
    directory = str(input("Directory: "))
    option = int(input("Select option: (1.basic/2.recursive): "))
    if option == 1:
        search_file(file, directory)
    elif option == 2:
        recursive_search(file, directory)
    else:
        print("Invalid option")

#buscar_archivo_simple("Readme.md","/Users/vicalons/Documents/PyC")

if __name__ == "__main__":
    main()