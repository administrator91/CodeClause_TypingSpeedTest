from tkinter import *
from tkinter import ttk
import time
import random
import difflib


class MainWindow:
    def __init__(self, root):
    
        self.text = ["Cybersecurity is the protection of internet-connected systems such as hardware, software and data from cyberthreads.",
                     "The practice is used by individuals and enterprises to protect against unauthorized access to data centers and other computerized systems.",
                     "The cybersecurity field can be broken down into several different sections, the coordination of which within the organization is crucial to the success of a cybersecurity program.",
                     "A vulnerability is a weakness in design, implementation, operation, or internal control. Most of the vulnerabilities that have been discovered are documented in the Common Vulnerabilities and Exposures (CVE) database.",
                     "A backdoor in a computer system, a cryptosystem, or an algorithm, is any secret method of bypassing normal authentication or security controls.",
                     "Phishing is the attempt of acquiring sensitive information such as usernames, passwords, and credit card details directly from users by deceiving the users.",
                     "Privilege escalation describes a situation where an attacker with some level of restricted access is able to, without authorization, elevate their privileges or access level",
                     "Reverse engineering is the process by which a man-made object is deconstructed to reveal its designs, code, and architecture, or to extract knowledge from the object.",
                     "Spoofing is an act of masquerading as a valid entity through the falsification of data.",
                     "Denial of service attacks (DoS) are designed to make a machine or network resource unavailable to its intended users."]
        self.speed = 0            #### DEFAULT ####
        self.accuracy = 0         #### DEFAULT ####
        self.time_start = 0       #### DEFAULT ####
        self.time_end = 0         #### DEFAULT ####
        root.title("Typing Speed calculator made by Rajarshi")
        ###################### FIG ############################################
        root.minsize(500, 500)
        ###
        for row in range(5):
            root.grid_rowconfigure(row, weight=1)
        for col in range(3):
            root.grid_columnconfigure(col, weight=1)
        self.label_text = Label(
            root, text="Hey Buddy!! Welcome to my typing speed calculator", wraplength=500)
        self.label_text.grid(row=0, column=0, columnspan=3, sticky="nsew")

        self.user_text = Text(root)
        self.user_text.grid(column=0, row=1, columnspan=3, sticky="nsew")
########################### BUTTON'S HERE ############################
        self.btn_start = Button(root, text="Start/Restart", command=self.start)
        self.btn_start.grid(column=0, row=2, columnspan=1, sticky="nsew")
        self.btn_stop = Button(root, text="Stop", command=self.stop)
        self.btn_stop.grid(column=1, row=2, columnspan=1, sticky="nsew")
        self.btn_newtext = Button(root, text="New Text", command=self.new_text)
        self.btn_newtext.grid(column=2, row=2, columnspan=1, sticky="nsew")
################################## RESULT ############################
        self.label_speed = Label(
            root, text=f"Your typing speed is {self.speed} WPM")
        self.label_speed.grid(row=3, column=0, columnspan=3, sticky="nsew")

        self.label_accuracy = Label(
            root, text=f"Your typing accuracy is {self.speed} %")
        self.label_accuracy.grid(row=4, column=0, columnspan=3, sticky="nsew")
#####################(BUTTON) CALCULATE logic FUNCTION #######################
    def start(self):
        self.time_start = time.time()
        
    def stop(self):
        self.time_end = time.time()
        words = self.label_text.cget("text").split(' ')
        self.speed = round(len(words)/((self.time_end - self.time_start)/60))
        self.label_speed.config(
            text=f"Your typing Speed is {self.speed} WPM")
        self.accuracy = round(difflib.SequenceMatcher(None, self.label_text.cget(
            "text"), self.user_text.get("1.0", 'end-1c')).ratio()*100)
        self.label_accuracy.config(
            text=f"Your typing accuracy is {self.accuracy} %")
        
    def new_text(self):
        self.label_text.config(
            text=self.text[random.randint(0, len(self.text)-1)])
        self.user_text.delete('1.0', END)
############# MAIN HERE #####################
def main():
    root = Tk()
    myapp = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()