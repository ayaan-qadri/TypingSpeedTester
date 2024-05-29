from tkinter import messagebox

def register(self):
    username = self.entry_username.get()
    password = self.entry_password.get()

    if not username or not password:
        messagebox.showerror(
            "Error", "Please enter both username and password", parent=self.app2)
        return

    self.cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    
    if self.cursor.fetchone():
        messagebox.showerror(
            "Error", "Username already exists. Please choose another.", parent=self.app2)
        return
    
    self.cursor.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    
    messagebox.showinfo("Success", "Registration successful",parent=self.app2)
