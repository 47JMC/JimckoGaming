import os # Operating System Library
import shutil # File Mover Library

user = os.getlogin() # Get windows username
default_dir = f"C:/Users/{user}/OneDrive/Desktop"

not_whitelisted = [
    "C:/Users/jarah/Downloads/",
    "C:/Users/jarah/Downloads"
]

def Organise(home_folder_path, destination_folder_path: str, extension_endswith: str):
    if home_folder_path not in not_whitelisted:
        files = os.listdir(home_folder_path)
        length = len(files)
        moveable = 0
        print(f"Found {length} Files")
        for file in files:
            if file.endswith(extension_endswith):
                moveable = moveable +1
                print(f"Moving {file} to {destination_folder_path}")
                shutil.move(os.path.join(home_folder_path, file), destination_folder_path)
        print(f"Targeted {moveable} files")

    else:
        print(f"{home_folder_path} is not whitelisted. Due to certain reasons with the windows file system")
        exit()

organiser_dir = input("Provide the path to the directory where the files you want to organise exist:")

if organiser_dir == "":
    print("Using Default Directory: Desktop")
    organiser_dir = default_dir

target_dir = input("Provide the path to the directory where the files will go to:")

if target_dir == "":
    print("Stopping Because of Required Option not filled")
    exit()

extension = input("Which files with the extension do you want to move (Example: .py .mp3)")

if extension == "":
    print("Stopping Because of Required Option not filled")
    exit()

Organise(organiser_dir, target_dir, extension)
# Organise(organiser_dir, f"C:/Users/{user}/Music/Playlists", (".mp3",".wav"))
