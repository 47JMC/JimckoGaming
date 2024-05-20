#========================
#    File Organiser
#========================
#Libraries
import os
import shutil

def Organise(home_folder, destination_folder):
    files = os.listdir(home_folder) 
    for file in files:
        if file.endswith((".mp3", ".wav")):
            shutil.move(os.path.join(home_folder, file), destination_folder)
            print(f"Moved {file} to {destination_folder}")

organiser_dir = input("Provide the path to the directory where the files you want to organise exist:")
if organiser_dir == "" or organiser_dir == " ":
    organiser_dir = f"C:/Users/{os.getlogin()}/Downloads/Organiser"
print(organiser_dir)

if os.path.exists(organiser_dir):
    Organise(organiser_dir, f"C:/Users/{os.getlogin()}/Music/Playlists")
else:
    os.mkdir(organiser_dir)
    print("Created Folder Organiser in ", organiser_dir)