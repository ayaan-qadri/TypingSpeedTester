from tkinter import messagebox
def login(self):
    self.username = self.entry_username.get()
    password = self.entry_password.get()

    if not self.username or not password:
        messagebox.showerror(
            "Error", "Please enter both username and password",parent=self.app2)
        return
        
    self.cursor.execute(
        "SELECT * FROM users WHERE username = %s AND password = %s", (self.username, password))
    
    if self.cursor.fetchone():
        messagebox.showinfo("Success", "Login successful",parent=self.app2)
        self.app2.destroy()
        self.isLoggedIn = True
        self.history.configure(state="normal")
        self.reset.configure(state="normal")

    else:
        messagebox.showerror("Error", "Invalid username or password",parent=self.app2)
