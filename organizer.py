import os
import shutil

FOLDER = input("Enter folder path: ")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

if not os.path.exists(FOLDER):
    print("Folder not found!")
    exit()

for file in os.listdir(FOLDER):
    file_path = os.path.join(FOLDER, file)

    if os.path.isfile(file_path):
        extension = os.path.splitext(file)[1].lower()

        for folder_name, extensions in file_types.items():
            if extension in extensions:
                destination = os.path.join(FOLDER, folder_name)

                if not os.path.exists(destination):
                    os.makedirs(destination)

                shutil.move(file_path, os.path.join(destination, file))
                print(f"Moved {file} -> {folder_name}")

print("Done! Files organized successfully.")
