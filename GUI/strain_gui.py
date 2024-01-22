import tkinter as tk
from tkinter import Spinbox, Button, Label, StringVar, Text, ttk

class Strain_gui:
    def __init__(self, root):
        self.root = root
        self.root.title("Strain Testing Bed")
        self.root.geometry("400x300")  # Adjust the window size as needed
        self.root.resizable(False, False)  # Make the window non-resizable

        # Styles
        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", background="#2196F3", foreground="white")
        self.style.configure("TLabel", padding=6, font=('Helvetica', 12, 'bold'))  # Bold for the first 4 labels
        self.style.configure("TProgressbar", thickness=20)

        # Labels
        self.label1 = ttk.Label(root, text="Cycles")
        self.label2 = ttk.Label(root, text="Position")
        self.label3 = ttk.Label(root, text="Initial")
        self.label4 = ttk.Label(root, text="Final")

        # Spinboxes
        self.spinbox1 = Spinbox(root, from_=0, to=10)
        self.spinbox2 = Spinbox(root, from_=0, to=10)
        self.spinbox3 = Spinbox(root, from_=0, to=10)
        self.spinbox4 = Spinbox(root, from_=0, to=10)

        # Buttons
        self.button1 = ttk.Button(root, text="Calibrate", command=self.on_button1_click)
        self.button2 = ttk.Button(root, text="Move", command=self.on_button2_click)

        # Progressbar
        self.progressbar = ttk.Progressbar(root, length=400, mode='indeterminate')

        # Label with text
        self.label_text1 = ttk.Label(root, text="Cycles: 0")
        self.label_text1.grid(row=8, column=0, columnspan=2, pady=5)  # Moved below the "Start" button

        # Additional Label with text
        self.label_text2 = ttk.Label(root, text="Position(mm): 0.0")
        self.label_text2.grid(row=9, column=0, columnspan=2, pady=5)  # New Label Text

        # Configure Grid Layout
        self.label1.grid(row=0, column=0)
        self.label2.grid(row=0, column=1)
        self.spinbox1.grid(row=1, column=0)
        self.spinbox2.grid(row=1, column=1)
        self.button1.grid(row=2, column=0, pady=10)
        self.button2.grid(row=2, column=1, pady=10)
        self.label3.grid(row=3, column=0)
        self.label4.grid(row=3, column=1)
        self.spinbox3.grid(row=4, column=0)
        self.spinbox4.grid(row=4, column=1)
        self.progressbar.grid(row=6, column=0, columnspan=2, sticky='ew', pady=5)  # Add some separation
        self.progressbar.start()
        self.start_button = ttk.Button(root, text="Start", command=self.on_start_click)
        self.start_button.grid(row=7, column=0, columnspan=2, pady=10, sticky='ew')
        self.start_state = False  # Variable to track the state of the Start button

    def on_button1_click(self):
        # Action for button 1
        pass

    def on_button2_click(self):
        # Action for button 2
        pass

    def on_start_click(self):
        # Toggle the text between "Start" and "Stop"
        if self.start_state:
            self.start_button.config(text="Start")
            self.start_state = False
        else:
            self.start_button.config(text="Stop")
            self.start_state = True

# Create the main window
root = tk.Tk()

# Create an instance of the interface
strain_gui = Strain_gui(root)

# Configure the main loop of the interface
root.mainloop()
 
