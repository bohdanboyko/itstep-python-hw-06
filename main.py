import os
import os.path
import shutil

# Завдання 1: Вивести всі файли та піддиректорії поточної робочої директорії

print("Вміст поточної директорії:")

for item in os.listdir("."):
    print(item)


# Завдання 2: Створити директорію NewFolder
new_folder = "NewFolder"

if not os.path.exists(new_folder):
    os.mkdir(new_folder)
    print(f"\nДиректорію '{new_folder}' створено.")
else:
    print(f"\nДиректорія '{new_folder}' вже існує.")

def createDir(dirName):
    if not os.path.exists(dirName):
        os.makedirs(dirName)

# Завдання 3: Скопіювати files/data.txt у backup/data_copy.txt

createDir('backup')
source_file = os.path.join("", "data.txt")
destination_file = os.path.join("./backup", "data_copy.txt")

shutil.copy2(source_file, destination_file)

print("\nФайл data.txt успішно скопійовано в backup/data_copy.txt")


# Завдання 4: Перейменувати old_data.txt на new_data.txt
old_file = os.path.join("", "data.txt")
new_file = os.path.join("", "old_data.txt")

shutil.copy2(old_file, new_file)

old_file = os.path.join("", "old_data.txt")
new_file = os.path.join("", "new_data.txt")

if os.path.isfile(new_file):
    os.remove(new_file)

os.rename(old_file, new_file)

print("Файл old_data.txt перейменовано на new_data.txt")


# Завдання 5: Перемістити important_data.txt у директорію backup
old_file = os.path.join("", "data.txt")
new_file = os.path.join("", "important_data.txt")

shutil.copy2(old_file, new_file)

file_to_move = "important_data.txt"
backup_file_name = os.path.join("./backup", file_to_move)

shutil.move(file_to_move, backup_file_name)

print("Файл important_data.txt переміщено в директорію backup.")

