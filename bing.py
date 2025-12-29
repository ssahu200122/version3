

import math
import random
import customtkinter
import threading
import time
import pyautogui
import pygetwindow as gw
import json
from slider import Slider
import subprocess
from slider1 import Slider1
import os
import platform

# from my_ordered_set import SortedProfileDict
import sys
from wonderwords import RandomWord
from cmd_colors import Colors


colors = Colors()


    

r = RandomWord()

widgets = {}

# Check if an argument was provided
# if len(sys.argv) > 1:
#     argument = sys.argv[1]  # First argument (after the script name)
#     both = int(argument)
# else:
#     both = 0


# if both == 1:
#     file = open('data1.json','r+')
#     profiles = json.load(file)
# else:
file = open('data.json','r+')
profiles = json.load(file)

selected_profiles = profiles.copy()



#Functions:

def save_profiles():
    global profiles
    pr = get_edge_profiles()
    # print(pr)
    profiles = json.dumps(pr, indent=2)
    # print(profiles)
    file.seek(0)
    file.write(profiles)
    file.truncate()

def restart_program():
    home_dir = os.path.expanduser('~')
    
    # Path for a desktop synced with OneDrive
    onedrive_desktop_path = os.path.join(home_dir, 'OneDrive', 'Desktop', 'newBing.bat')
    
    # Path for a standard local desktop
    local_desktop_path = os.path.join(home_dir, 'Desktop', 'newBing.bat')

    # Check if the OneDrive path exists and use it, otherwise use the local path
    if os.path.exists(onedrive_desktop_path):
        batch_file = onedrive_desktop_path
    else:
        batch_file = local_desktop_path
        
    # Run the batch file
    os.system(f'start "" "{batch_file}"')

def kill_program():
    sys.exit("Stopping program")


def draw_widgets():
    global widgets

    # destroy previous drawn profiles:
    for widget in fr1.winfo_children():
        widget.destroy()

    # print(profiles)
    #Redraw profiles:
    for i,profile in enumerate(profiles):
        # print(i,profile)
        
        
        s = Slider(fr1,profile=f"{profile}",v=(profiles[profile]["PcPoints"],profiles[profile]["MobilePoints"]),profiles=profiles,cmd=profiles[profile]["cmd"],profiles_set=selected_profiles,mbox=all_checkbox)
        s.grid(row=i+5,column=0,sticky='we')
        widgets[profile] = s

def shutdown_computer():
    # Check which operating system the computer is running
    current_os = platform.system()
    
    print(f"Detected OS: {current_os}")
    print("Shutting down...")

    if current_os == "Windows":
        # /s = shutdown, /t 0 = 0 seconds delay
        os.system("shutdown /s /t 0")
    elif current_os == "Linux" or current_os == "Darwin": # Darwin is macOS
        # -h = halt/shutdown, now = immediately
        # Note: This usually requires root/sudo privileges on Linux/Mac
        os.system("sudo shutdown -h now")
    else:
        print("Operating system not supported for automatic shutdown.")

def get_edge_profiles():
    profiles = {}
    edge_user_data_dir = os.path.expandvars(r"%LOCALAPPDATA%\\Microsoft\\Edge\\User Data")
    local_state_path = os.path.join(edge_user_data_dir, "Local State")

    try:
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = json.load(f)
    except FileNotFoundError:
        print("Edge 'Local State' file not found.")
        return {}

    prols = local_state.get("profile", {})
    info_cache = prols.get("info_cache", {})
    print(prols["profiles_order"])

    for i in prols["profiles_order"]:
        profiles[f"{info_cache[i]["user_name"]} ({info_cache[i]["shortcut_name"]})"] = {
    "cmd": "--profile-directory="+i,
    "PcPoints": 0,
    "MobilePoints": 75
  }
    return profiles

def open_edge_profiles(profile_list,m=False):
    base_command = ["Start", "msedge"]
    for profile in profile_list:
        subprocess.Popen(base_command + [profile], shell=True)
        

def search(win,m=False):
    win.activate()
    # print("# ",end=" ")
    time.sleep(0.5)
    if m:
        pyautogui.hotkey('ctrl',"tab")
    pyautogui.hotkey('ctrl',"e")
    pyautogui.write(r.word())
    pyautogui.press('enter')
    time.sleep(1)

def search1(win):
    win.activate()
    time.sleep(0.5)
    pyautogui.hotkey('ctrl',"l")
    pyautogui.write("https://rewards.bing.com/pointsbreakdown?form=edgepredeem")
    pyautogui.press('enter')
    time.sleep(1)

def get_edge_windows():
    time.sleep(5)  # Wait for Edge to launch
    all_windows = gw.getAllWindows()
    edge_windows = [win for win in all_windows if "Edge" in win.title]
    return edge_windows

def activate_inspectionmode():
    wins = get_edge_windows()
    for win in wins:
        win.activate()
        time.sleep(2)
        pyautogui.hotkey('ctrl','shift','i')
        time.sleep(3)
        pyautogui.hotkey('ctrl','t')
        time.sleep(1)
        pyautogui.hotkey('ctrl','shift','i')
        time.sleep(3)

    
        
def close_edge_windows():
    #  taskkill /IM msedge.exe /F >NUL 2>&1
    #  subprocess.run(['taskkill','/F','/IM','msedge.exe'])
    subprocess.run(['taskkill', '/F', '/IM', 'msedge.exe'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def all_checkbox_event():
    global selected_profiles
    if all_check_var.get() == "on":
        selected_profiles.clear()
        selected_profiles.update(profiles.copy())
        for profile in profiles:
            widgets[profile].check_var.set("on")
            
    else:
        selected_profiles.clear()
        for profile in profiles:
            widgets[profile].check_var.set("off")

    all_checkbox.configure(text="All: "+str(len(selected_profiles)))

def chech_checkbox_event():
    update_check()
    global check_flag
    if check_check_var.get() == "on":
        check_flag = len(selected_profiles)
    else:
        check_flag = 0

check_flag = len(selected_profiles)

def update_check(i=None,n=None):
    if not(i==None and n==None):
        check.configure(text=f"{i}-{i+n}")
    else:
        check.configure(text="Check")


def check_button():
    global check_flag
    print("yessss")
    close_edge_windows()

    if check_flag > 0 and check_check_var.get() == "on":
        i = len(selected_profiles) - check_flag
        n = numOfProfiles.var.get()

        # Update check button text immediately
        check.configure(text=f"{i}-{i+n}")

        # Start background thread for the rest of the work
        def background_task():
            time.sleep(0.5)
            all_cmds = [profile["cmd"] for profile in selected_profiles.values()]
            cmd_range = all_cmds[i:i+n]

            open_edge_profiles(cmd_range)
            for win in get_edge_windows():
                search1(win)

            
            global check_flag
            check_flag -= n
            if check_flag <= 0:
                check_check_var.set("off")
                check.configure(text="Check")

        threading.Thread(target=background_task).start()

        
def calculateSets():
    n = numOfProfiles.var.get()
    options = [f"{i}-{i+n}" for i in range(0,len(profiles),n)]
    return options

def optionmenu_callback(choice):
    if "inverse selection" == choice:
        inverse = set(profiles).difference(selected_profiles)

        if len(inverse) < len(profiles):
            all_check_var.set("off")
        else:
            all_check_var.set("on")

        for w in widgets.values():
            w.checkbox.toggle()
    elif choice == "selected":
        print(f"{len(selected_profiles)} PROFILES SELECTED..............:")
        for p in selected_profiles:
            print(p)

    elif choice == "Custom":
        dialog = customtkinter.CTkInputDialog(text="Type in format x-y:", title="Custom")
        # print("Number:", dialog.get_input())
        pair = list(map(int,dialog.get_input().split('-')))
        pair_profiles = list(profiles)[pair[0]:pair[1]+1]

        

        selected_profiles.clear()
        selected_profiles.update({profile: profiles[profile] for profile in pair_profiles if profile in profiles})


        if len(selected_profiles) < len(profiles):
            all_check_var.set("off")
        else:
            all_check_var.set("on")
        all_checkbox.configure(text="All: "+str(len(selected_profiles)))
        for profile in profiles:
            if profile in pair_profiles:
                widgets[profile].checkbox.select()
            else:
                widgets[profile].checkbox.deselect()
    elif choice == "Auto detect Profiles":
        save_profiles()
        restart_program()
        kill_program()

    else:
        pair = list(map(int,choice.split('-')))
        pair_profiles = list(profiles)[pair[0]:pair[1]]
        print(pair_profiles)

        selected_profiles.clear()
        selected_profiles.update({profile: profiles[profile] for profile in pair_profiles if profile in profiles})

        if len(selected_profiles) < len(profiles):
            all_check_var.set("off")
        else:
            all_check_var.set("on")


        all_checkbox.configure(text="All: "+str(len(selected_profiles)))
        for profile in profiles:
            if profile in pair_profiles:
                widgets[profile].checkbox.select()
            else:
                widgets[profile].checkbox.deselect()


def numOfProfiles_event():
    options = ["inverse selection","selected"]+calculateSets()+["Custom","Auto detect Profiles"]
    optionmenu.configure(values=options)



def start_button(start_test=False,kk=0):
    totalSearchedPoints = 0
    if start_test:n=4
    else:n = numOfProfiles.var.get()
    N = len(selected_profiles)
    print(N)
    for i in range(0,N,n):
        search_profiles = [profile["cmd"] for profile in selected_profiles.values()][i:i+n]

        if start_test:
            k=kk
        else:k = pc_slider.var.get()
        totalPoints = k*N
        pc = k//3
        print(f"{colors.color_256_bg(22)}{colors.color_256_fg(15)}{colors.BOLD}              ({(i//n)+1}/{math.floor(N/n)+1}"," Round started ",f"{i}-{i+n-1} [{totalSearchedPoints}/{totalPoints}])           {colors.RESET}")
        # totalSearchedPoints += n*k
        if pc:
            open_edge_profiles(search_profiles)
            # time.sleep(3)
            wins = get_edge_windows()

            for i in range(pc):
                for win in wins:
                    
                    search(win)
                    totalSearchedPoints += 3
                    
                    if len(search_profiles) <= 3:
                        time.sleep(2)
                str = "# "*len(wins)+"  "*(n-len(wins))
                print(f"{colors.YELLOW}{str} {colors.RESET}",end=" ")
                print(f"{colors.BG_BLUE}{colors.WHITE}{colors.BOLD}: ({(i+1)*3}/{pc_slider.var.get()}) [{totalSearchedPoints}/{totalPoints}]{colors.RESET}")
            time.sleep(2)
            close_edge_windows()

        time.sleep(2)
        if not start_test:
            m = mobile_slider.var.get()//3
            if m:
                open_edge_profiles(search_profiles)
                # time.sleep(3)
                activate_inspectionmode()


                wins = get_edge_windows()
                

                for _ in range(m):
                    for win in wins:
                        search(win,m=True)
                        time.sleep(1)
                        if len(search_profiles) <= 3:
                            time.sleep(2)

                
                time.sleep(2)
                close_edge_windows()
    print(f"{colors.BG_BRIGHT_YELLOW}{colors.BLACK}{colors.BOLD}                       DONE [{totalSearchedPoints}/{totalPoints}]                      {colors.RESET}")

    if shutdown_check_var.get() == "on" and not start_test:
        shutdown_computer()


if len(sys.argv)>1:
    print(sys.argv)
    start_button(True,int(sys.argv[1]))
else:
    #Main UI
    app = customtkinter.CTk()
    app.geometry("870x310+830+600")
    app.title("Bing Auto Search")
    # app.resizable(False,False)
    app.attributes("-topmost",True)

    app.grid_columnconfigure(0, weight=5)
    app.grid_columnconfigure(1, weight=3)
    app.grid_rowconfigure(0, weight=1)


    #Frame down:
    downfr = customtkinter.CTkFrame(app)
    downfr.grid(row=1,column=0,sticky="ew",padx=10,pady=5,columnspan=2)
    downfr.columnconfigure(0,weight=1)

    all_check_var = customtkinter.StringVar(value="on")
    all_checkbox = customtkinter.CTkCheckBox(downfr, text="All: "+str(len(selected_profiles)), command=all_checkbox_event,
                                        variable=all_check_var, onvalue="on", offvalue="off")
    all_checkbox.grid(row=0,column=0,padx=8,pady=5,sticky="w")


    check_check_var = customtkinter.StringVar(value="off")
    checkcheckbox = customtkinter.CTkCheckBox(downfr, text="", command=chech_checkbox_event,
                                        variable=check_check_var, onvalue="on", offvalue="off",width=10)
    checkcheckbox.grid(row=0,column=2,padx=5,pady=5,sticky="e")


    check = customtkinter.CTkButton(downfr,text="Check",font=("Cascadia code",15),fg_color="GREY",command=check_button)
    check.grid(row=0,column=3,padx=5,pady=5,sticky="e")

    closeb = customtkinter.CTkButton(downfr,text="Close",font=("Cascadia code",15),fg_color="GREEN",command=close_edge_windows)
    closeb.grid(row=0,column=4,padx=5,pady=5,sticky="e")

    shutdown_check_var = customtkinter.StringVar(value="off")
    shutdowncheckbox = customtkinter.CTkCheckBox(downfr, text="Shutdown",variable=shutdown_check_var, onvalue="on", offvalue="off")
    shutdowncheckbox.grid(row=0,column=5,padx=5,pady=5,sticky="e")

    start = customtkinter.CTkButton(downfr,text="Start",font=("Cascadia code",15),command=start_button)
    start.grid(row=0,column=6,padx=5,pady=5,sticky="e")


    #Frame 1:
    fr1 = customtkinter.CTkScrollableFrame(app)
    fr1.grid(row=0,column=0,sticky="nsew",padx=(10,5),pady=5)


    draw_widgets()
    #Frame 2:
    fr2 = customtkinter.CTkScrollableFrame(app)
    fr2.grid(row=0,column=1,sticky="nsew",padx=(5,10),pady=10)


    fr2.columnconfigure(0,weight=1)
    fr2.rowconfigure(0,weight=1)

    numOfProfiles = Slider1(fr2,"Number of profiles: ",2,15,1,7,command=numOfProfiles_event)
    numOfProfiles.grid(row=0,column=0,sticky="swe",padx=20,pady=(5,2))

    pc_slider = Slider1(fr2,"PC: ",0,102,3,random.choice(range(6,30,3)))
    pc_slider.grid(row=1,column=0,sticky="swe",padx=20,pady=3)

    mobile_slider = Slider1(fr2,"Mobile: ",0,75,3,0)
    mobile_slider.grid(row=2,column=0,sticky="swe",padx=20,pady=(2,5))

    optionmenu_var = customtkinter.StringVar(value="inverse selection")
    options = ["inverse selection","selected"]+calculateSets()+["Custom","Auto detect Profiles"]
    optionmenu = customtkinter.CTkOptionMenu(downfr,values=options,
                                            command=optionmenu_callback,
                                            variable=optionmenu_var)
    optionmenu.grid(row=0,column=1,padx=5,pady=5,sticky="w")

    app.mainloop()