# ui.py created by Jacob Humston                    #
# Includes code snippets gathered from generator.py #
# MIT (See LICENSE)                                 #

### MODULES #########################################
import customtkinter
import webbrowser


### Variables #######################################
SWITCH_TOKEN = "OThmN2U0MmMyZTNhNGY4NmE3NGViNDNmYmI0MWVkMzk6MGEyNDQ5YTItMDAxYS00NTFlLWFmZWMtM2U4MTI5MDFjNGQ3"
UI = customtkinter.CTk()


### Setup UI #######################################
UI.title("Fortnite.GG Locker Generator")
UI.geometry("400x400")
UI.resizable(False, False)
UI.iconbitmap("./icon.ico")

WELCOME_LABEL = customtkinter.CTkLabel(UI, text="Welcome! To get started, press the button below to \nauthorize with Epic Games.", fg_color="transparent", font=("Arial", 14), pady=5)
WELCOME_LABEL.pack()

### Start the Main Loop ############################
UI.mainloop()