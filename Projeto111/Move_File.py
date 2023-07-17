import os
import shutil

from_dir = "C:/Users/Leandro Oliveira/Desktop/path1"
to_dir = "C:/Users/Leandro Oliveira/Desktop/path2"

allowed_extensions = ['.txt', '.doc', '.docx', '.pdf', '.lua']

files_to_move = []

for file_name in os.listdir(from_dir):
    name, extension = os.path.splitext(file_name)
    
    if extension in allowed_extensions:
        files_to_move.append(file_name)

if not os.path.exists(to_dir):
    os.makedirs(to_dir)

for file_name in files_to_move:
    path1 = os.path.join(from_dir, file_name)
    path2 = os.path.join(to_dir, file_name)
    
    print("Movendo", file_name)
    shutil.move(path1, path2)
