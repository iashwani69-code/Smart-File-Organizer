import os
import shutil
import hashlib

# File categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}


def get_folder_path():
    """Ask the user for the folder path."""
    return input("Enter folder path: ")


def create_folder(base_folder, folder_name):
    """Create a folder if it does not exist."""
    folder_path = os.path.join(base_folder, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path


def get_file_hash(file_path):
    """Generate a unique hash for a file."""
    hasher = hashlib.md5()

    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)

            if not chunk:
                break

            hasher.update(chunk)

    return hasher.hexdigest()


def organize_files(folder_path):
    """Move files into folders based on extension."""

    if not os.path.exists(folder_path):
        print("Folder not found!")
        return

    hashes = {}

    duplicate_folder = create_folder(folder_path, "Duplicates")

    for file_name in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file_name)

        if not os.path.isfile(file_path):
            continue

        file_hash = get_file_hash(file_path)

        # Duplicate check
        if file_hash in hashes:
            shutil.move(
                file_path,
                os.path.join(duplicate_folder, file_name)
            )
            print(f"Duplicate moved: {file_name}")
            continue

        hashes[file_hash] = file_name

        extension = os.path.splitext(file_name)[1].lower()

        moved = False

        for folder_name, extensions in FILE_TYPES.items():

            if extension in extensions:

                destination = create_folder(
                    folder_path,
                    folder_name
                )

                shutil.move(
                    file_path,
                    os.path.join(destination, file_name)
                )

                print(f"Moved: {file_name} → {folder_name}")

                moved = True
                break

        if not moved:
            other_folder = create_folder(folder_path, "Others")

            shutil.move(
                file_path,
                os.path.join(other_folder, file_name)
            )

            print(f"Moved: {file_name} → Others")

    print("\nOrganization Completed Successfully!")


def main():
    print("=" * 40)
    print(" SMART FILE ORGANIZER ")
    print("=" * 40)

    folder_path = get_folder_path()

    organize_files(folder_path)


if __name__ == "__main__":
    main()
