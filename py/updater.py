# ======= Imports =======
# External Functions
import os

# =================== Start Program ========================
print("Controleren of er updates zijn...\n")
# installing all the requirements
cmd_output1 = os.popen("pip install -r requirements.txt --disable-pip-version-check").read()
# git pull with my personal access token always the main branch
update_data = os.popen("git pull https://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@github.com/DjodyKort/AscendantSurvival-leveling.git main").read()

if "Already up to date" in update_data:
    print("\nAlle updates zijn al gedaan en er zijn geen updates op dit moment!\n")
else:
    print(update_data)