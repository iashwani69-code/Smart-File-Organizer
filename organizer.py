import os
import shutil

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

def get_folder_path():
    folder = input("Enter folder path: ")
    return folder

def create_destination_folder(base_folder, folder_name):
    destination = os.path.join(base_folder, folder_name)
    if not os.path.exists(destination):
        os.makedirs(destination)
    return destination

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("Folder not found!")
        return

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            extension = os.path.splitext(file_name)[1].lower()

            for folder_name, extensions in FILE_TYPES.items():
                if extension in extensions:
                    destination_folder = create_destination_folder(folder_path, folder_name)
                    shutil.move(file_path, os.path.join(destination_folder, file_name))
                    print(f"Moved {file_name} -> {folder_name}")
                    break

    print("Done! Files organized successfully.")

def main():
    folder_path = get_folder_path()
    organize_files(folder_path)

if __name__ == "__main__":
    main()
