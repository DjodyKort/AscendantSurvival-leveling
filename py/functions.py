# ========= Imports =========
import pyautogui
import time


# ============= Functions =============
# Normal functions
def ShiftClick():
    pyautogui.keyDown('shift')
    pyautogui.click()
    pyautogui.keyUp('shift')


def KeyDownAndUp(key):
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)

# Main functions
def UnarmedLeveling():
    while True:
        while pyautogui.locateOnScreen('images/iron.png', grayscale=False, confidence=0.5,
                                       region=(600, 970, 64, 64)) is not None:
            for i in range(1, 7):
                pyautogui.click()
                time.sleep(0.4)
            for i in range(1, 5):
                pyautogui.rightClick()
        # Opening inventory and putting new stack of iron in offhand
        KeyDownAndUp('e')
        time.sleep(0.2)
        # If there is no iron in inventory, then quit the program
        if pyautogui.locateOnScreen('images/IronInv.png', grayscale=False, confidence=0.5,
                                    region=(712, 520, 494, 240)) is None:
            quit()
        # If there is iron in inventory, then move to it and click it
        location = pyautogui.locateOnScreen('images/IronInv.png', grayscale=False, confidence=0.5,
                                            region=(712, 520, 494, 240))
        pyautogui.moveTo(location.left + location.width / 2, location.top + location.height / 2)
        KeyDownAndUp('f')
        KeyDownAndUp('e')


def RepairLeveling():
    # ================ Declaring Variables ================
    hotbar_helmet_location = [720, 704, 48, 48]
    hotbar_chestplate_location = [774, 704, 48, 48]
    hotbar_leggings_location = [828, 704, 48, 48]
    hotbar_boots_location = [882, 704, 48, 48]

    # ================ Start of Function ================
    while True:
        # Declaring Variables
        broken_helmet_location = pyautogui.locateOnScreen('images/broken_helmet.png', grayscale=False, confidence=0.99,
                                                          region=(720, 302, 48, 48))
        broken_chestplate_location = pyautogui.locateOnScreen('images/broken_chestplate.png', grayscale=False,
                                                              confidence=0.99,
                                                              region=(720, 356, 48, 48))
        broken_leggings_location = pyautogui.locateOnScreen('images/broken_leggings.png', grayscale=False,
                                                            confidence=0.99,
                                                            region=(720, 410, 48, 48))
        broken_boots_location = pyautogui.locateOnScreen('images/broken_boots.png', grayscale=False, confidence=0.99,
                                                         region=(720, 464, 48, 48))
        # Start Program
        if broken_helmet_location is not None:
            print("Broken Helmet Found! Fixing it now!\n")
            # Moving mouse to helmet and clicking 1 on it
            pyautogui.moveTo(broken_helmet_location.left + broken_helmet_location.width / 2,
                             broken_helmet_location.top + broken_helmet_location.height / 2)
            # Putting it in hotbar and equipping it in hand
            KeyDownAndUp('1')
            KeyDownAndUp('e')
            KeyDownAndUp('1')
            #  Reparing helmet
            for i in range(1, 7):
                pyautogui.rightClick()
            # Going to inventory and putting helmet on head again
            KeyDownAndUp('e')
            time.sleep(0.2)
            pyautogui.moveTo(hotbar_helmet_location[0] + hotbar_helmet_location[2] / 2,
                             hotbar_helmet_location[1] + hotbar_helmet_location[3] / 2)
            ShiftClick()

        if broken_chestplate_location is not None:
            print("Broken Chestplate Found! Fixing it now!\n")
            # Moving mouse to chestplate and clicking 2 on it
            pyautogui.moveTo(broken_chestplate_location.left + broken_chestplate_location.width / 2,
                             broken_chestplate_location.top + broken_chestplate_location.height / 2)
            # Putting it in hotbar and equipping it in hand
            KeyDownAndUp('2')
            KeyDownAndUp('e')
            KeyDownAndUp('2')
            #  Reparing chestplate
            for i in range(1, 7):
                pyautogui.rightClick()
            # Going to inventory and putting chestplate on chest again
            KeyDownAndUp('e')
            time.sleep(0.2)
            pyautogui.moveTo(hotbar_chestplate_location[0] + hotbar_chestplate_location[2] / 2,
                             hotbar_chestplate_location[1] + hotbar_chestplate_location[3] / 2)
            ShiftClick()

        if broken_leggings_location is not None:
            print("Broken Leggings Found! Fixing it now!\n")
            # Moving mouse to leggings and clicking 3 on it
            pyautogui.moveTo(broken_leggings_location.left + broken_leggings_location.width / 2,
                             broken_leggings_location.top + broken_leggings_location.height / 2)
            # Putting it in hotbar and equipping it in hand
            KeyDownAndUp('3')
            KeyDownAndUp('e')
            KeyDownAndUp('3')
            #  Reparing leggings
            for i in range(1, 7):
                pyautogui.rightClick()
            # Going to inventory and putting leggings on legs again
            KeyDownAndUp('e')
            time.sleep(0.2)
            pyautogui.moveTo(hotbar_leggings_location[0] + hotbar_leggings_location[2] / 2,
                             hotbar_leggings_location[1] + hotbar_leggings_location[3] / 2)
            ShiftClick()

        if broken_boots_location is not None:
            print("Broken Boots Found! Fixing it now!\n")
            # Moving mouse to boots and clicking 4 on it
            pyautogui.moveTo(broken_boots_location.left + broken_boots_location.width / 2,
                             broken_boots_location.top + broken_boots_location.height / 2)
            # Putting it in hotbar and equipping it in hand
            KeyDownAndUp('4')
            KeyDownAndUp('e')
            KeyDownAndUp('4')
            #  Reparing boots
            for i in range(1, 7):
                pyautogui.rightClick()
            # Going to inventory and putting boots on feet again
            KeyDownAndUp('e')
            time.sleep(0.2)
            pyautogui.moveTo(hotbar_boots_location[0] + hotbar_boots_location[2] / 2,
                             hotbar_boots_location[1] + hotbar_boots_location[3] / 2)
            ShiftClick()