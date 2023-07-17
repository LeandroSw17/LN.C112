import os
import shutil

from_dir = "C:/Users/Leandro Oliveira/Desktop/path1"
to_dir = "C:/Users/Leandro Oliveira/Desktop/path2"

allowed_extensions = ['.txt', '.doc', '.docx', '.pdf', '.lua']

# Lista de arquivos que serão movidos
files_to_move = []

# Percorrer todos os arquivos no diretório de origem
for file_name in os.listdir(from_dir):
    name, extension = os.path.splitext(file_name)
    
    # Verificar se a extensão é permitida
    if extension in allowed_extensions:
        files_to_move.append(file_name)

# Criar o diretório de destino se ainda não existir
if not os.path.exists(to_dir):
    os.makedirs(to_dir)

# Mover os arquivos para a pasta de destino
for file_name in files_to_move:
    path1 = os.path.join(from_dir, file_name)
    path2 = os.path.join(to_dir, file_name)
    
    print("Movendo", file_name)
    shutil.move(path1, path2)
