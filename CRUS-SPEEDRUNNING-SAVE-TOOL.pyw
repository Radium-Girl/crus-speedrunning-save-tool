import os
import tkinter as tk
import subprocess
from tkinter import messagebox, filedialog
import json

# FILE PATHS
user = os.getlogin()
savegame_path = f"C:\\Users\\{user}\\AppData\\Roaming\\Godot\\app_userdata\\Cruelty Squad\\savegame.save"
stocks_path = f"C:\\Users\\{user}\\AppData\\Roaming\\Godot\\app_userdata\\Cruelty Squad\\stocks.save"
config_path = f"C:\\Users\\{user}\\AppData\\Roaming\\Godot\\app_userdata\\Cruelty Squad\\config.json"

# SAVE AND LOAD GAME DIR
def load_game_directory():
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
            return config.get("game_directory")
    return None

# DELETE SAVE
def delete_files():
    try:
        if os.path.exists(savegame_path):
            os.remove(savegame_path)
        if os.path.exists(stocks_path):
            os.remove(stocks_path)
        messagebox.showinfo("SUCCESS", "SAVE DELETED")
    except Exception as e:
        messagebox.showerror("ERROR", f"AN ERROR OCCURRED: {e}")

# MAKE PRACTICE SAVE
def create_savegame():
    try:
        if os.path.exists(savegame_path):
            if not messagebox.askyesno("OVERWRITE CONFIRMATION", "DOING THIS WILL OVERWRITE YOUR CURRENT SAVE DATA, ARE YOU SURE?"):
                return
        with open(savegame_path, "w") as file:
            file.write("""{"Alpine Hospitality_hell_raw_stime":99999999,"Alpine Hospitality_hell_raw_time":99999999,"Alpine Hospitality_hell_string_stime":"N/A","Alpine Hospitality_hell_string_time":"N/A","Alpine Hospitality_raw_stime":99999999,"Alpine Hospitality_raw_time":99999999,"Alpine Hospitality_string_stime":"N/A","Alpine Hospitality_string_time":"N/A","Androgen Assault_hell_raw_stime":99999999,"Androgen Assault_hell_raw_time":99999999,"Androgen Assault_hell_string_stime":"N/A","Androgen Assault_hell_string_time":"N/A","Androgen Assault_raw_stime":99999999,"Androgen Assault_raw_time":99999999,"Androgen Assault_string_stime":"N/A","Androgen Assault_string_time":"N/A","Apartment Atrocity_hell_raw_stime":99999999,"Apartment Atrocity_hell_raw_time":99999999,"Apartment Atrocity_hell_string_stime":"N/A","Apartment Atrocity_hell_string_time":"N/A","Apartment Atrocity_raw_stime":99999999,"Apartment Atrocity_raw_time":99999999,"Apartment Atrocity_string_stime":"N/A","Apartment Atrocity_string_time":"N/A","Archon Grid_hell_raw_stime":99999999,"Archon Grid_hell_raw_time":99999999,"Archon Grid_hell_string_stime":"N/A","Archon Grid_hell_string_time":"N/A","Archon Grid_raw_stime":99999999,"Archon Grid_raw_time":99999999,"Archon Grid_string_stime":"N/A","Archon Grid_string_time":"N/A","Bog Business_hell_raw_stime":99999999,"Bog Business_hell_raw_time":99999999,"Bog Business_hell_string_stime":"N/A","Bog Business_hell_string_time":"N/A","Bog Business_raw_stime":99999999,"Bog Business_raw_time":99999999,"Bog Business_string_stime":"N/A","Bog Business_string_time":"N/A","Casino Catastrophe_hell_raw_stime":99999999,"Casino Catastrophe_hell_raw_time":99999999,"Casino Catastrophe_hell_string_stime":"N/A","Casino Catastrophe_hell_string_time":"N/A","Casino Catastrophe_raw_stime":99999999,"Casino Catastrophe_raw_time":99999999,"Casino Catastrophe_string_stime":"N/A","Casino Catastrophe_string_time":"N/A","Cruelty Squad Headquarters_hell_raw_stime":99999999,"Cruelty Squad Headquarters_hell_raw_time":99999999,"Cruelty Squad Headquarters_hell_string_stime":"N/A","Cruelty Squad Headquarters_hell_string_time":"N/A","Cruelty Squad Headquarters_raw_stime":99999999,"Cruelty Squad Headquarters_raw_time":99999999,"Cruelty Squad Headquarters_string_stime":"N/A","Cruelty Squad Headquarters_string_time":"N/A","Darkworld_hell_raw_stime":99999999,"Darkworld_hell_raw_time":99999999,"Darkworld_hell_string_stime":"N/A","Darkworld_hell_string_time":"N/A","Darkworld_raw_stime":99999999,"Darkworld_raw_time":99999999,"Darkworld_string_stime":"N/A","Darkworld_string_time":"N/A","House_hell_raw_stime":99999999,"House_hell_raw_time":99999999,"House_hell_string_stime":"N/A","House_hell_string_time":"N/A","House_raw_stime":99999999,"House_raw_time":99999999,"House_string_stime":"N/A","House_string_time":"N/A","Idiot Party_hell_raw_stime":99999999,"Idiot Party_hell_raw_time":99999999,"Idiot Party_hell_string_stime":"N/A","Idiot Party_hell_string_time":"N/A","Idiot Party_raw_stime":99999999,"Idiot Party_raw_time":99999999,"Idiot Party_string_stime":"N/A","Idiot Party_string_time":"N/A","Mall Madness_hell_raw_stime":99999999,"Mall Madness_hell_raw_time":99999999,"Mall Madness_hell_string_stime":"N/A","Mall Madness_hell_string_time":"N/A","Mall Madness_raw_stime":99999999,"Mall Madness_raw_time":99999999,"Mall Madness_string_stime":"N/A","Mall Madness_string_time":"N/A","Miner's Miracle_hell_raw_stime":99999999,"Miner's Miracle_hell_raw_time":99999999,"Miner's Miracle_hell_string_stime":"N/A","Miner's Miracle_hell_string_time":"N/A","Miner's Miracle_raw_stime":99999999,"Miner's Miracle_raw_time":99999999,"Miner's Miracle_string_stime":"N/A","Miner's Miracle_string_time":"N/A","Neuron Activator_hell_raw_stime":99999999,"Neuron Activator_hell_raw_time":99999999,"Neuron Activator_hell_string_stime":"N/A","Neuron Activator_hell_string_time":"N/A","Neuron Activator_raw_stime":99999999,"Neuron Activator_raw_time":99999999,"Neuron Activator_string_stime":"N/A","Neuron Activator_string_time":"N/A","Office_hell_raw_stime":99999999,"Office_hell_raw_time":99999999,"Office_hell_string_stime":"N/A","Office_hell_string_time":"N/A","Office_raw_stime":99999999,"Office_raw_time":99999999,"Office_string_stime":"N/A","Office_string_time":"N/A","Paradise_hell_raw_stime":99999999,"Paradise_hell_raw_time":99999999,"Paradise_hell_string_stime":"N/A","Paradise_hell_string_time":"N/A","Paradise_raw_stime":99999999,"Paradise_raw_time":99999999,"Paradise_string_stime":"N/A","Paradise_string_time":"N/A","Pharmakokinetiks_hell_raw_stime":99999999,"Pharmakokinetiks_hell_raw_time":99999999,"Pharmakokinetiks_hell_string_stime":"N/A","Pharmakokinetiks_hell_string_time":"N/A","Pharmakokinetiks_raw_stime":99999999,"Pharmakokinetiks_raw_time":99999999,"Pharmakokinetiks_string_stime":"N/A","Pharmakokinetiks_string_time":"N/A","Seaside Shock_hell_raw_stime":99999999,"Seaside Shock_hell_raw_time":99999999,"Seaside Shock_hell_string_stime":"N/A","Seaside Shock_hell_string_time":"N/A","Seaside Shock_raw_stime":99999999,"Seaside Shock_raw_time":99999999,"Seaside Shock_string_stime":"N/A","Seaside Shock_string_time":"N/A","Sin Space Engineering_hell_raw_stime":99999999,"Sin Space Engineering_hell_raw_time":99999999,"Sin Space Engineering_hell_string_stime":"N/A","Sin Space Engineering_hell_string_time":"N/A","Sin Space Engineering_raw_stime":99999999,"Sin Space Engineering_raw_time":99999999,"Sin Space Engineering_string_stime":"N/A","Sin Space Engineering_string_time":"N/A","Trauma Loop_hell_raw_stime":99999999,"Trauma Loop_hell_raw_time":99999999,"Trauma Loop_hell_string_stime":"N/A","Trauma Loop_hell_string_time":"N/A","Trauma Loop_raw_stime":99999999,"Trauma Loop_raw_time":99999999,"Trauma Loop_string_stime":"N/A","Trauma Loop_string_time":"N/A","bonus_unlocked":["House","Darkworld","Alpine Hospitality","God","Club","END"],"consecutive_deaths":0,"dead_npcs":[],"death":false,"ending_1":false,"ending_2":false,"ending_3":false,"hell_discovered":false,"hope":false,"husk":false,"implants_unlocked":["Grappendix","Eyes of Corporate Insight","Nightmare Vision Goggles","Speed Enhancer Gland","Speed Enhancer Node Cluster","Speed Enhancer Total Organ Package","CSIJ Level II Body Armor","CSIJ Level IV Body Armor","Zomy X-200 Portable Cassette Player","Biothruster","CSIJ Level III Body Armor","CSIJ Level V Biosuit","Extravagant Suit","Military Camouflage","Stealth Suit","Load Bearing Vest","Tactical Blast Shield","House","Composite Helmet","Zoom N Go Bionic Eyes","Life Sensor","Skullgun","Vertical Entry Device","Pneumatic Legs","Alien Leg Wetware","Augmented arms","First Aid Kit","ZZzzz Special Sedative Grenade","Ammunition Gland","Angular Advantage Tactical Munitions","Gunkboosters","Flechette Grenade","HE Grenade","Icaros Machine","CSIJ Level IIB Body Armor","Cursed Torch","Night Vision Goggles","Microbial Oil Secretion Glands","Hazmat Suit","Flowerchute","Tattered Rain Hat","Bouncy Suit","Funkgrunters","Goo Overdrive","CSIJ Level VI Golem Exosystem","Cortical Scaledown+","Abominator","Holy Scope","Biojet"],"items_found":[],"levels_punished":[true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true],"levels_unlocked":12,"money":999999499,"play_time":154368,"soul":false,"weapons_unlocked":[true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true]}""")
        messagebox.showinfo("SUCCESS", "PRACTICE SAVE CREATED")
    except Exception as e:
        messagebox.showerror("ERROR", f"AN ERROR OCCURRED: {e}")

# OPEN SAVEGAME DIRECTORY
def open_savegame_directory():
    savegame_dir = os.path.dirname(savegame_path)
    if os.path.exists(savegame_dir):
        subprocess.Popen(f'explorer "{savegame_dir}"')
    else:
        messagebox.showerror("ERROR", "SAVEGAME DIRECTORY NOT FOUND.")

# GUI
app = tk.Tk()
app.title("SAVEGAME TOOL")
app.geometry("500x200")
app.resizable(False, False)

# GRID
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)
app.columnconfigure(2, weight=1)
app.rowconfigure(0, weight=1)
app.rowconfigure(1, weight=1)
app.rowconfigure(2, weight=1)
app.rowconfigure(3, weight=1)

# LABEL AND BUTTONS
label = tk.Label(app, text="CRUS SPEEDRUNNING TOOL", font=("SimSun-ExtB", 24))
label.grid(row=0, column=0, columnspan=3, pady=10, padx=20, sticky="n")

# BUTTONS
buttons_frame = tk.Frame(app)
buttons_frame.grid(row=1, column=0, columnspan=3, pady=5, padx=20)

open_dir_button = tk.Button(buttons_frame, text=" 📂 ", command=open_savegame_directory, font=("SimSun-ExtB", 12), bg="black", fg="#ff00c8")
open_dir_button.grid(row=0, column=0, padx=1, pady=5)

delete_button = tk.Button(buttons_frame, text="   DELETE SAVE   ", command=delete_files, font=("SimSun-ExtB", 12), bg="black", fg="green")
delete_button.grid(row=0, column=1, padx=1, pady=5)

create_button = tk.Button(buttons_frame, text="CREATE PRACTICE SAVE", command=create_savegame, font=("SimSun-ExtB", 12), bg="green", fg="red")
create_button.grid(row=1, column=0, columnspan=2, pady=5, padx=20, sticky="ew")

app.mainloop()
