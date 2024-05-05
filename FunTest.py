#======================
#   Fun Project
#======================
import os #Library for files
import subprocess #Library for commands
import sqlite3 #SQLite3 Database library

#Defining the music directories
musicdirs = ["Default","Custom"]
order_musicdirs = "\n".join(musicdirs)

#Defining and ordering music files
default_dir = "C:/Users/jarah/Music/Playlists"
order_default_dir = "\n".join(os.listdir(default_dir))

#SQlite3 settings
conn = sqlite3.connect('funinfo.db')
cursor = conn.cursor()

def play_music(path):
    # Play the music file
    subprocess.Popen(["ffplay", path])

#Ask for name
name = input("Enter Your Name:\n")
data_name = name.replace(" ","-")
cursor.execute(f"CREATE TABLE IF NOT EXISTS {name} (dummy_column TEXT)")

# Developer Settings
project_devs = ["Jabir"]
def check_project_developer(dev_name):
    if dev_name in project_devs:
        return True
    return False

#Defining and ordering counters
if check_project_developer:
    counters = ["Mobile & Laptop Counter","Music Counter","Display Database Info"]
else:
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
            cursor.execute(f"INSERT INTO {name} VALUES (?)", (music_file_path,))
            conn.commit()

            #Play the music
            play_music(music_file_path)

        else:
            print("could not find file")

    elif select_music_dir.lower() == "custom":
        select_music_files = input(f"Enter the path to the music file you want to play:\n")
        if os.path.exists(select_music_files):
            cursor.execute(f"INSERT INTO {name} VALUES (?)", (select_music_files,))
            conn.commit()
            play_music(select_music_files)

        else:
            print("could not find file")

elif counter.lower() == "display database info" or counter.lower() == "dev":
    if check_project_developer(name):
        table_name = input("Enter a Table's Name:\n")

        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    else:
        print("You are not a developer")
else:
    print("Error.How did you reach here?")
