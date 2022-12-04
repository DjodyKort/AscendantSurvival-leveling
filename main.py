# ========== Imports ==========
from py.updater import update_data
from py.functions import *
import time

# ========== Declaring Variables ==========
which_leveling = None

# ========== Start of Program ==========
# Checking which leveling to do
while True:
    which_leveling = input("Which leveling do you want to do? (Unarmed/Repair):\n\n").lower()
    if which_leveling == "unarmed" or which_leveling == "repair":
        break
    else:
        print("Please enter a valid option.\n")
        continue

print("Do 5 things:\n\n1. Don't have your game in fullscreen. Just Maximize it.\n2. Have your GUI scale on large or 3\n3. Have your monitor on 1920x1080 resolution\n4. Wear your armor and have Diamonds\n5. Have your first 4 hotbar slots free!1e1\n\nYou have 10 seconds :)\n")
time.sleep(10)
print("Program started....\n")
# Activating the correct leveling process
if which_leveling == "unarmed":
    UnarmedLeveling()
elif which_leveling == "repair":
    RepairLeveling()
