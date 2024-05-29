import customtkinter as ctk

def user(self,root):
    self.app2 = ctk.CTkToplevel(root)
    self.app2.title("User")
    self.app2.attributes('-topmost', 'true')
    self.app2.geometry('%dx%d+%d+%d'%(self.width, self.height, self.x, self.y))
    self.app2.resizable(False, False)
    self.app2.grab_set()

    self.userFrame = ctk.CTkFrame(self.app2,width=400,height=300,fg_color="transparent")
    self.userFrame.pack(pady=(self.y/2,0))

    self.label_username = ctk.CTkLabel(self.userFrame, text="Username:",bg_color="transparent",font=("",17))
    self.label_username.grid(row=0, column=0, padx=10, pady=10)
    
    self.entry_username = ctk.CTkEntry(self.userFrame,height=30)
    self.entry_username.grid(row=0, column=1, pady=10)
    
    self.label_password = ctk.CTkLabel(self.userFrame, text="Password:",font=("",17))
    self.label_password.grid(row=1, column=0,padx=10,pady=10)
    
    self.entry_password = ctk.CTkEntry(self.userFrame,height=30, show="*")
    self.entry_password.grid(row=1, column=1, pady=10)
    
    button_register = ctk.CTkButton(
        self.app2, text="Register", command=self.register)
    button_register.pack(pady=(10,0))
    
    button_login = ctk.CTkButton(
        self.app2, text="Login", command=self.login)
    button_login.pack(pady=10)
    self.app2.grab_set()
    self.app2.mainloop()
