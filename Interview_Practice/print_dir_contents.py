import os

sPath = input("Enter path to search: ")

def print_directory_contents(sPath):
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)

        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)

print_directory_contents(sPath)