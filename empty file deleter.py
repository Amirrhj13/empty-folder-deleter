import os

def emptydeleter(directory):
    direct = os.path.isdir(directory)
    if direct == True:
        for folder in os.listdir(directory):
            folder = os.path.join(directory,folder)
            if not os.listdir(folder):
                os.rmdir(folder)
            else:
                continue
    else:
        print("The Directory doesn't exist")

    return directory

directory = input("input directory: ")
emptydeleter(directory)