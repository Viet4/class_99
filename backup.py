import os
import shutil

source = input("Source Folder Name: ")
destination = input("Destination Folder Name: ")

source = source + "/"
destination = destination + "/"

list_of_files = os.listdir(source)

for files in list_of_files:
    shutil.copy((source + files), destination)
    