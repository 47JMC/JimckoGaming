#======================
#   Fun Project
#======================
import os #Library for files
import subprocess #Library for commands

#Defining the music directories
musicdirs = ["Default","Custom"]
order_musicdirs = "\n".join(musicdirs)

#Defining and ordering music files
user = os.getlogin()
default_dir = f"C:/Users/{user}/Music/Playlists"
order_default_dir = "\n".join(os.listdir(default_dir))

def play_music(path):
    try:
        # Play the music file
        subprocess.Popen(["ffplay", path])
    except Exception as e:
        print("Please install FFMPEG and add it to your PATH. Try again")

#Ask for name
name = input("Enter Your Name:\n")
data_name = name.replace(" ","-")

#Counters
counters = ["Mobile & Laptop Counter","Music Counter"]
#Order all counters
order_counters = "\n".join(counters)

counter = input(f"Hello {name}.Enter the counter you want to go to:\n\n{order_counters}\n\n")

if counter.lower() == "mobile & laptop counter" or counter.lower() == "mobile counter" or counter.lower() == "laptop counter":

    buy_items = ["IPhone 14 Pro Max","Samsung S24 Ultra","Redmibook 15 Pro","Saptop 12 Pro","Sapple M75 Ultra Max","GalaxyGaming"]
    order_buy_items = "\n".join(buy_items)

    if name == "Jabir":
        costs = ["₹0","₹0","₹0","₹0","₹0","₹0"]
    else:
        costs = ["₹1,25,000","₹1,18,999","₹45,000","₹32,999","₹2,00,000","₹15,000"]

    item = input(f"Hello {name}, What would you like to buy?\n\n{order_buy_items}\n\n")
    if item in buy_items:
        print(f"Ordered {item}")
        print(f"The cost of {item} is {costs[buy_items.index(item)]}")
    else:
        print("Item not found in list!!.Please run the script again")

elif counter.lower() == "music counter" or counter.lower() == "music":
    order_default_dir = "\n".join(os.listdir(default_dir))
    select_music_dir = input(f"Choose a music folder to play music:\n\n{order_musicdirs}\n\n")

    if select_music_dir.lower() == "default":
        select_music_files = input(f"Select a File that you want to play:\n\n{order_default_dir}\n\n")
        music_file_path = os.path.join(default_dir, select_music_files)
        
        if os.path.exists(music_file_path):
            
            #Play the music
            play_music(music_file_path)

        else:
            print("could not find file")

    elif select_music_dir.lower() == "custom":
        select_music_files = input(f"Enter the path to the music file you want to play:\n")
        if os.path.exists(select_music_files):
            
            play_music(select_music_files)

        else:
            print("could not find file")

else:
    print("Error.How did you reach here?")
