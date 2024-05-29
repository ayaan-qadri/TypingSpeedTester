import customtkinter as ctk
import random
import time
from tkinter import messagebox
import mysql.connector
import sys
import json
from LogNReg.login import login as lg
from LogNReg.register import register as rg
from LogNReg.userDesign import user as userDesign
from ui import setup_ui as mainUi

class CurrentHistory:

    def __init__(self,atTimeDate,timeTook,speed,accuracy,totalWords,wellWords):
        self.atTimeDate = atTimeDate
        self.timeTook = timeTook
        self.speed = speed
        self.accuracy = accuracy
        self.totalWords = totalWords
        self.wellWords = wellWords

class TypingSpeedTester:

    def __init__(self, root,cursor):
        self.root = root
        self.cursor = cursor
        self.width = 800
        self.height = 450
        self.root.title("Typing Speed Tester")

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.x = (self.screen_width/2) - (self.width/2)
        self.y = (self.screen_height/2) - (self.height/2)
        self.root.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))
        self.root.resizable(False, False)
        self.isLoggedIn = False
        self.current_sentence = ""
        self.user_input = ctk.StringVar()
        self.start_time = None
        self.timer_label = ctk.CTkLabel(self.root, text="")
        self.typing_speed_label = ctk.CTkLabel(self.root, text="")
        self.accuracy_label = ctk.CTkLabel(self.root, text="")
        self.word_count_label = ctk.CTkLabel(self.root, text="")
        self.correct_word_count = 0
        self.total_word_count = 0
        self.showCount = False
        self.app2 = None
        self.time_count = 1
        self.setup_ui()

    def choose_random_sentence(self):
        self.cursor.execute("SELECT sentence FROM sentences")
        sentences = cursor.fetchall()

        random_sentence = random.choice(sentences)[0]
        self.current_sentence = random_sentence

    def setup_ui(self):
        mainUi(self,root)

    def user(self):
        userDesign(self,root)
   
    def register(self):
        rg(self)
        try:
            db.commit()
        except:
            messagebox.showerror(f"Can not register, TRY AGAIN.",parent=self.app2)
    
    def login(self):
        lg(self)
   
    def save(self):
        formatted_time = time.strftime("%Y-%m-%d %I:%M:%S %p", time.localtime())
        cHistory = CurrentHistory(str(formatted_time),self.time_count,self.words_per_minute,self.accuracy,self.total_word_count,self.correct_word_count)
        cHistoryObj =  cHistory.__dict__
        
        jsonRObj = []
        
        historyQ = self.cursor.execute(f"SELECT history FROM users WHERE username = '{self.username}'")
        # self.cursor.execute(historyQ) 
        fetchData = self.cursor.fetchone()[0]
        
        if(fetchData != None):
            jsonRObj = json.loads(fetchData.decode('ascii'))['data']
            jsonRObj.append(cHistoryObj)
            toJson = json.dumps({"data":jsonRObj})
            currentData = f"UPDATE users SET history = '{toJson}' WHERE users.username = '{self.username}'"
            cursor.execute(currentData)
            db.commit()
        else:
            data = json.dumps({"data":[cHistoryObj]})
            currentData = f"UPDATE users SET history = '{data}' WHERE users.username = '{self.username}'"
            cursor.execute(currentData)
            db.commit()
        self.save.configure(text="Saved",state="disabled")

    def history(self):
        self.cursor.execute(f"SELECT history From users WHERE username='{self.username}'")
        res = self.cursor.fetchone()
        if(res[0] == None):
           messagebox.showinfo(
               "No Records", "No Records Found", parent=self.root)
           return
        historyBox = ctk.CTkToplevel(self.root)
        historyBox.attributes("-topmost", True)
    
        historyBox.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))    
        historyBox.resizable(False,False)
        historyBox.grab_set()

        historyFrame = ctk.CTkScrollableFrame(historyBox,width=770,height=400)
        historyFrame.pack()
        
        indexT = ctk.CTkLabel(historyFrame,text="INDEX",corner_radius=5, fg_color="#8103ff")
        indexT.grid(row=0, column=0, padx=10, pady=10)
        
        tNdT = ctk.CTkLabel(historyFrame, text="WHEN",corner_radius=5, fg_color="#8103ff")
        tNdT.grid(row=0, column=1, padx=10, pady=10)
        
        timeTookT = ctk.CTkLabel(historyFrame, text="TIME TOOK",corner_radius=5, fg_color="#8103ff")
        timeTookT.grid(row=0, column=2, padx=10, pady=10)
        
        speedT = ctk.CTkLabel(historyFrame, text="SPEED",corner_radius=5, fg_color="#8103ff")
        speedT.grid(row=0, column=3, padx=10, pady=10)
        
        accuracyT = ctk.CTkLabel(historyFrame, text="ACCURACY",corner_radius=5, fg_color="#8103ff")
        accuracyT.grid(row=0, column=4, padx=10, pady=10)
        
        totalWordsT = ctk.CTkLabel(historyFrame, text="TOTAL WORDS",corner_radius=5, fg_color="#8103ff")
        totalWordsT.grid(row=0, column=5, padx=10, pady=10)
        
        wellWordsT = ctk.CTkLabel(historyFrame, text="CORRECT WORDS",corner_radius=5, fg_color="#8103ff")
        wellWordsT.grid(row=0, column=6, padx=10, pady=10)
        
        rowCount = 1
        for t in json.loads(res[0].decode('ascii'))['data']:
            
            no = ctk.CTkLabel(historyFrame, text=rowCount,corner_radius=5,text_color="#000000", fg_color="#d3d3d3")
            no.grid(row=rowCount, column=0, padx=10, pady=10)

            atTimeDate = ctk.CTkLabel(historyFrame, text=t['atTimeDate'],corner_radius=5,text_color="#000000", fg_color="#d3d3d3")
            atTimeDate.grid(row=rowCount, column=1,padx=10, pady=10)
            
            timeTook = ctk.CTkLabel(
                historyFrame, text=f"{t['timeTook']} seconds", corner_radius=5, text_color="#000000", fg_color="#d3d3d3")
            timeTook.grid(row=rowCount, column=2,padx=10, pady=10)
            
            speed = ctk.CTkLabel(historyFrame, text=f"{t['speed']} WPM",corner_radius=5,text_color="#000000", fg_color="#d3d3d3")
            speed.grid(row=rowCount, column=3,padx=10, pady=10)
            
            accuracy = ctk.CTkLabel(historyFrame, text=f"{t['accuracy']}%",corner_radius=5,text_color="#000000", fg_color="#d3d3d3")
            accuracy.grid(row=rowCount, column=4,padx=10, pady=10)
            
            totalWords = ctk.CTkLabel(historyFrame, text=t['totalWords'],corner_radius=5,text_color="#000000", fg_color="#d3d3d3")
            totalWords.grid(row=rowCount, column=5,padx=10, pady=10)
            
            wellWords = ctk.CTkLabel(historyFrame, text=t['wellWords'],corner_radius=5,text_color="#000000", fg_color="#d3d3d3")
            wellWords.grid(row=rowCount, column=6,padx=10, pady=10)
        
            rowCount = rowCount + 1

        historyBox.mainloop()
  
    def start_typing_test(self):

        if not self.isLoggedIn:
            
            if self.app2 == None:
                self.user()
                self.first = False
            else:
                if self.app2.winfo_exists():
                    messagebox.showwarning("Warning","Please login.")
                else:
                    self.user()

        else:
            self.reset_ui()
            self.entry_user_input.configure(state='normal')
            self.button_start.configure(text='Change sentence')
            self.choose_random_sentence()
            # self.current_sentence = random.choice(self.sentences)
            self.label_sentence.configure(text=self.current_sentence)
            self.total_word_count = len(self.current_sentence.split())
            self.user_input.set("")
            self.start_time = time.time()
            self.correct_word_count = 0
            self.showCount = True
            self.root.bind("<Return>", self.check_typing_speed)
            self.entry_user_input.configure(state='normal')
            self.history.configure(state="disabled")
            self.update_timer()
    
    def reset_ui(self):
        self.label_sentence.configure(text="")
        self.typing_speed_label.configure(text="")
        self.accuracy_label.configure(text="")
        self.word_count_label.configure(text="")
        self.button_start.configure(state='normal')
        self.button_start.configure(text='Start Testing')
        self.user_input.set("")
        self.start_time = None
        self.showCount = False
        self.timer_label.configure(text='')
        self.save.configure(text="Save",state='disabled')
        self.entry_user_input.configure(state='disabled')
        self.history.configure(state="normal")
    
    def check_typing_speed(self, event):
        
        if self.start_time is not None:
            end_time = time.time()
            elapsed_time = end_time - self.start_time

            user_text = self.user_input.get()
            typed_words = len(user_text.split())
            self.words_per_minute = int((typed_words / elapsed_time) * 60)
            self.accuracy = self.calculate_accuracy(
                self.current_sentence, user_text)

            speed_message = f"Typing speed: {self.words_per_minute} WPM"
            accuracy_message = f"Accuracy: {self.accuracy}%"

            self.typing_speed_label.configure(text=speed_message)
            self.accuracy_label.configure(text=accuracy_message)

            original_words = self.current_sentence.split()
            user_words = user_text.split()
            self.correct_word_count = sum(1 for w1, w2 in zip(
                original_words, user_words) if w1 == w2)

            self.display_word_tracking()

            # Unbind the Enter key to prevent multiple calculations
            self.root.unbind("<Return>")

            self.entry_user_input.configure(state='disabled')

            self.showCount = False
    
    def update_timer(self):
        if self.showCount:
            timeCount = time.time() - self.start_time
            self.time_count = round(timeCount) + 1
            self.timer_label.configure(
                text=f"Countdown : {self.time_count} seconds")
            try:
                self.root.after(1000, self.update_timer)
            except:
                sys.exit(1)

    def calculate_accuracy(self, original, user_text):
        self.history.configure(state="normal")
        self.save.configure(text="Save",state="normal")
        self.button_start.configure(text='Re-start')
        original_words = original.split()
        user_words = user_text.split()
        correct_words = sum(1 for w1, w2 in zip(
            original_words, user_words) if w1 == w2)
        total_words = len(original_words)
        accuracy = (correct_words / total_words) * 100
        return round(accuracy, 2)

    def display_word_tracking(self):
        word_count_message = f"Words: {self.correct_word_count} / {self.total_word_count}"
        self.word_count_label.configure(text=word_count_message)

if __name__ == "__main__":

    
    try:
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tst"
        )
        cursor = db.cursor(buffered=True)

        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), history JSON)")

        cursor.execute("CREATE TABLE IF NOT EXISTS sentences (sentence VARCHAR(255))")
        
        root = ctk.CTk()
        app = TypingSpeedTester(root,cursor)
        ctk.set_appearance_mode("dark")
        root.mainloop()
    except mysql.connector.Error as err:
        messagebox.showerror("Connection Error",f"Error - {err}")