print("Now loadings...")
"""Common shared code used in pipelines."""
import os

# for GUI
import PySimpleGUI as sg
import re
from pathlib import Path
import sys

# for rude.exe
import subprocess
import pyautogui
import time

# Define GUI "key" objects list as menu.
menu = ["-START-"]

# Special function for PyInstaller to contain additional files at _MEIPASS module of sys.
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


# Define PySimpleGUI's theme 
sg.theme_add_new("AUGMENT", {
        'BACKGROUND': '#f08080', # Coca-Cola Red color
        'TEXT': 'white',
        'INPUT': '#dedede',
        'SCROLL': '#dedede',
        'TEXT_INPUT': 'black',
        'BUTTON': ('black', 'white'),
        'PROGRESS': sg.DEFAULT_PROGRESS_BAR_COLOR,
        'BORDER': 1,
        'SLIDER_DEPTH': 0,
        'PROGRESS_DEPTH': 0}
        )

sg.theme("AUGMENT")
# Layout and window setup
layout = [
    [
        sg.Output(size=(50, 20), key='-OUT-'),
        sg.VerticalSeparator(),
        sg.Column([
            [sg.Text("　　　　")],
            [sg.Text("　　　　")],
            #[sg.Image(filename=resource_path("rude.png"))],
            [
                sg.Column([
                    [sg.Text("　　　　")],
                    [sg.Text("       ")],
                    [sg.Text("File path :")],
                    [sg.Text("　　　　")],
                    [sg.Text("　　　　")],
                ]),
                sg.Column([
                    [sg.Text("　　　　")],
                    [sg.Text("       ")],
                    [sg.Text(fr'C:\Users\{os.getlogin()}\AppData\Local\Microsoft\Teams\Update.exe')],
                    [sg.Text("　　　　")],
                    [sg.Text("　　　　")],
                ])
            ],
            [sg.Text()], # Empty line
            [sg.Button("Start", font=("Helvetica",24), size=(10,0), key="-START-")],
            [sg.Button("Stop", font=("Helvetica",24), size=(10,0), key="-STOP-")]
        ], element_justification="center"), 
    ]
]
window = sg.Window("Rude -Auto Teams Activation Tool-", layout=layout)



def auto_teams_login():
    def autotype():
        pyautogui.moveTo(800,35) # Cursor on to serch box
        time.sleep(5) # Wait until Teams starts
        pyautogui.click() # Click search box
        keyword = "Auto Type"
        for word in keyword:
            pyautogui.typewrite(word)
        pyautogui.press('enter')
        time.sleep(3)

#    def open_teams():
#        windows_user = os.getlogin()
#        subprocess.Popen(fr'C:\Users\{windows_user}\AppData\Local\Microsoft\Teams\Update.exe --processStart "Teams.exe"') # Open Teams
#        pyautogui.moveTo(800,40) # Cursor on to serch box
#        time.sleep(5) # Wait until Teams starts
#        pyautogui.click() # Click search box

    def open_teams():
        pyautogui.hotkey('winleft', 's')
        time.sleep(2)
        search_word = "Teams"
        for words in search_word:
            pyautogui.typewrite(words)
        time.sleep(4)
        pyautogui.press('enter')
        time.sleep(6)
        pyautogui.hotkey('winleft', 'up')


    def clear_text():
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('delete')

    def execute_function():
        open_teams()
        while True:
            try:
                autotype()
                clear_text()
            except KeyboardInterrupt:
                print('ctrl c')
                break
    execute_function()


def printr(text):
    """Custom print function to refresh window after every print."""
    print(text)
    window.refresh()



# Job Section
# Define variables
def main():
    # Introductory message
    window.finalize() # Finalize python GUI window before update specific window.
    window['-OUT-'].update("Welcome to Rude -Auto Teams Activation Tool-!\nDo you want to enjoy your daily life? Press \"Start\" to begin. Enjoy!\n\n")
    
    # Event loop
    while True:
        event, value = window.read()
        # print('イベント:',event ,', 値:',values) # for debug
        if event in (sg.WINDOW_CLOSED,):
            window.close()
            sys.exit(0)
        if event in ("-START-"):
            # Confirm pop up 
            response = sg.popup_yes_no(f"Do you want to proceed?", keep_on_top=True, background_color="lightgray", text_color="black")
            if response == 'Yes': 
                printr("\n=== Rude program is Running ===\n")
                print(f"\nStarting Rude.exe job.\n")
                auto_teams_login()                   
            else: 
                printr("Oh you are good contributer of CCBJI!\n")
                continue # And pushed back to the top of while loop.
        if event in ("-STOP-"):
            window.close()
            sys.exit(0)


if __name__ == "__main__":
    main()



