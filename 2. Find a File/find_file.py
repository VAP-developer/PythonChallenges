# Program: Find a file
# Basic: Current directory
# Medium: Recursive search
# Advance: (*.txt)

import os

# Basic search
#------------------------------------------------------------------
def search_file(file_name, directory):
    files = os.listdir(directory)
    if file_name in files:
        print("Find!")
    else:
        print("Dont find :(")

# Medium
#------------------------------------------------------------------
def ft_walk(dir):
    result = []
    files = []
    dirs = []
    root = [dir]
    dir_complete = os.listdir(dir)
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

# Program
#------------------------------------------------------------------
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

if __name__ == "__main__":
    main()