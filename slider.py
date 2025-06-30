import customtkinter
import tkinter
import subprocess
import pyautogui
import time




class Slider(customtkinter.CTkFrame):
    def __init__(self,master,cmd=None,to=120,v=(60,30),profile=None,profiles=None,profiles_set=None,mbox=None):
        super().__init__(master=master)
        # self.columnconfigure(0,weight=1)
        self.cmd = cmd

        # self.commd = commd
        self.fg_color = self.cget("fg_color")
        self.profile = profile
        self.profiles = profiles
        self.profiles_set = profiles_set
        self.mbox = mbox
     

        italic_underline_font = customtkinter.CTkFont(family="Helvetica", size=18, slant="italic", underline=True)

        self.check_var = customtkinter.StringVar(value="on")
        self.checkbox = customtkinter.CTkCheckBox(self,text="", command=self.checkbox_event,
                                     variable=self.check_var, onvalue="on", offvalue="off",width=10)
        self.checkbox.grid(row=0,column=0)

        self.head = customtkinter.CTkLabel(self,text=self.profile,font=italic_underline_font,text_color="cyan")
        self.head.grid(row=0,column=1)

        self.head.bind('<Button>',self.openProfile)
        self.head.bind("<Enter>", self.on_enter)
        self.head.bind("<Leave>", self.on_leave)
        self.focus = "null"


    def on_enter(self,event):
        self.head.configure(text_color="yellow")

# Function to handle hover leave
    def on_leave(self,event):
        self.head.configure(text_color="cyan")

    
    def openProfile(self,e):
        subprocess.run(['start','msedge',self.cmd],shell=True)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl','l')
        pyautogui.write("https://rewards.bing.com/pointsbreakdown?form=edgepredeem")
        pyautogui.press('enter')


    def setFocus(self,a):
        self.focus = a
    def setFocusOut(self,e):
        self.focus = None

    def setActive(self):
        self.configure(fg_color="yellow")
    
    def setDeactive(self):
        self.configure(fg_color=self.fg_color)

    def checkbox_event(self):
        if self.check_var.get() == "on":
            self.profiles_set.update({self.profile:self.profiles[self.profile]})
        else:
            if self.profile in self.profiles_set:
                del self.profiles_set[self.profile]

        if len(self.profiles_set)<len(self.profiles):
            self.mbox.deselect()
        else:
            self.mbox.select()

        self.mbox.configure(text="All: "+str(len(self.profiles_set)))


    

        
        


        