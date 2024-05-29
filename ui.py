import customtkinter as ctk

def setup_ui(self,root):

    
    self.label_sentence = ctk.CTkLabel(
        self.root, text="", justify="center", font=("Helvetica", 20))
    self.label_sentence.pack(pady=30)

    self.entry_user_input = ctk.CTkEntry(
        self.root,state= "disabled",textvariable=self.user_input, width=270, height=40, font=("System", 17),fg_color='#121212')
    self.entry_user_input.pack(pady=10,padx=10)

    btnFrame = ctk.CTkFrame(self.root,fg_color='transparent')
    btnFrame.columnconfigure(0,weight=0)

    self.button_start = ctk.CTkButton(
        btnFrame, text="Start Testing", width=30, height=30, font=("System", 17), command=self.start_typing_test, fg_color='#121212', hover_color='#7b7b7b')
    self.button_start.grid(row=0,column=0,padx=10)

    self.reset = ctk.CTkButton(
        btnFrame, text="Reset", state="disabled", width=30, height=30, font=("System", 17), command=self.reset_ui, fg_color='#121212', hover_color='#7b7b7b')
    self.reset.grid(row=0,column=1,padx=10)
    
    self.save = ctk.CTkButton(
        btnFrame, text="Save", state = "disabled",width=30, height=30, font=("System", 17), command=self.save, fg_color='#121212', hover_color='#7b7b7b')
    self.save.grid(row=0, column=2, padx=10)
    
    self.history = ctk.CTkButton(
        btnFrame, text="History", state="disabled",width=20,height=30, font=("System", 17), command=self.history, fg_color='#121212', hover_color='#7b7b7b')
    self.history.grid(row=1, column=1, padx=10,pady=10)


    btnFrame.pack(pady=10)
    self.timer_label.pack()
    self.typing_speed_label.pack()
    self.accuracy_label.pack()
    self.word_count_label.pack()
