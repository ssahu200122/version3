import customtkinter

class Slider1(customtkinter.CTkFrame):
    def __init__(self, master,text,start,end,step,value,command=None):
        super().__init__(master)

        self.command = command

        # self.columnconfigure(0,weight=1)

        self.var = customtkinter.IntVar()
        self.var.set(value)

        self.label = customtkinter.CTkLabel(self,text=text,font=("Cascadia code",15))
        self.label.grid(row=0,column=0,padx=20,pady=(5,2),sticky="w")

        self.slider = customtkinter.CTkSlider(self, from_=start, to=end,variable=self.var,command=self.slider_event,number_of_steps=(end-start)//step)
        self.slider.grid(row=1,column=0,sticky="swe",padx=20,pady=(3,5))

        self.slider_label = customtkinter.CTkLabel(self,text=str(int(self.var.get())),font=("Cascadia code",15))
        self.slider_label.grid(row=1,column=1,sticky="swe",padx=5,pady=(3,5))

    def slider_event(self,value):
        self.slider_label.configure(text=int(value))
        if self.command:
            self.command()