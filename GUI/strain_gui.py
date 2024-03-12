import tkinter as tk
from tkinter import Spinbox, Button, Label, StringVar, Text, ttk
import serial
import serial.tools.list_ports
import time

# Constants
CALIBRATE = 'a'
HOME = 'b'
MOVE = 'c'
OSCILLATE = 'd'

class StrainGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Strain Testing Bed")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        # Styles
        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", background="#2196F3", foreground="white")
        self.style.configure("TLabel", padding=6, font=('Helvetica', 12, 'bold'))
        self.style.configure("TProgressbar", thickness=20)

        # Labels
        self.label1 = ttk.Label(root, text="Cycles")
        self.label2 = ttk.Label(root, text="Position")
        self.label3 = ttk.Label(root, text="Initial")
        self.label4 = ttk.Label(root, text="Final")

        # Spinboxes
        self.spinbox1 = Spinbox(root, from_=1, to=5000, increment=1)
        self.spinbox2 = Spinbox(root, from_=0, to=100, increment=0.004)
        self.spinbox3 = Spinbox(root, from_=0, to=100, increment=0.004)
        self.spinbox4 = Spinbox(root, from_=0, to=100, increment=0.004)

        # ComboBox for serial ports
        self.serial_ports = self.get_serial_ports()
        self.serial_var = StringVar(value=self.serial_ports[0] if self.serial_ports else "")
        self.serial_combobox = ttk.Combobox(root, textvariable=self.serial_var, values=self.serial_ports)

        # Buttons
        self.button1 = ttk.Button(root, text="Calibrate", command=self.on_button1_click)
        self.button2 = ttk.Button(root, text="Move", command=self.request_translation)
        self.button3 = ttk.Button(root, text="Start", command=self.on_start_click)
        self.connect_button = ttk.Button(root, text="Connect", command=self.toggle_serial_connection)

        # Progressbar
        self.progressbar = ttk.Progressbar(root, length=400, mode='indeterminate')

        # Configure Grid Layout
        self.serial_combobox.grid(row=0, column=0, pady=5)
        self.connect_button.grid(row=0, column=1, pady=5)
        self.label1.grid(row=1, column=0)
        self.label2.grid(row=1, column=1)
        self.spinbox1.grid(row=2, column=0)
        self.spinbox2.grid(row=2, column=1)
        self.button1.grid(row=3, column=0, pady=10)
        self.button2.grid(row=3, column=1, pady=10)
        self.label3.grid(row=4, column=0)
        self.label4.grid(row=4, column=1)
        self.spinbox3.grid(row=5, column=0)
        self.spinbox4.grid(row=5, column=1)
        self.progressbar.grid(row=6, column=0, columnspan=2, sticky='ew', pady=5)
        self.progressbar.start()
        self.button3.grid(row=7, column=0, columnspan=2, pady=10, sticky='ew')  

        # Labels with text
        self.label_text1 = ttk.Label(root, text="Cycles: 0")
        self.label_text1.grid(row=8, column=0, columnspan=2, pady=5)  

        self.label_text2 = ttk.Label(root, text="Position(mm): 0.0")
        self.label_text2.grid(row=9, column=0, columnspan=2, pady=5)  

        self.start_state = False


    def get_serial_ports(self):
        try:
            ports = [port.device for port in serial.tools.list_ports.comports() if port.device]
            return ports
        except Exception as e:
            print(f"Error getting serial ports: {e}")
            return []

    def toggle_serial_connection(self):
        if hasattr(self, 'serial_connection') and self.serial_connection.is_open:
            self.stop_serial_connection()
        else:
            selected_port = self.serial_var.get()
            if selected_port:
                if self.start_serial_connection(selected_port):
                    print(f"Connected to {selected_port}")
                else:
                    print("Error starting serial connection.")
            else:
                print("Select a serial port before connecting.")

    def start_serial_connection(self, port):
        try:
            self.serial_connection = serial.Serial(port, baudrate=115200, timeout=1)
            self.connect_button.config(text="Disconnect")
            return True
        except Exception as e:
            print(f"Error starting serial connection: {e}")
            return False

    def stop_serial_connection(self):
        try:
            if hasattr(self, 'serial_connection') and self.serial_connection.is_open:
                self.serial_connection.close()
                print("Serial connection closed.")
                self.connect_button.config(text="Connect")
        except Exception as e:
            print(f"Error closing serial connection: {e}")
    
    def on_button1_click(self):
        self.calibrate_window = tk.Toplevel(self.root)
        self.calibrate_window.title("Warning")
        label_message = ttk.Label(self.calibrate_window, text="Calibration: Be careful to not break the sensor!")
        label_message.grid(row=0, column=0, padx=10, pady=10)
        button_ok = ttk.Button(self.calibrate_window, text="OK", command=self.send_calibrate)
        button_ok.grid(row=1, column=0, padx=10, pady=10)
        
    def send_calibrate(self):
        if hasattr(self, 'serial_connection') and self.serial_connection.is_open:
            try:
                self.serial_connection.write(b'a')  
                print("Calibration requested")
            except Exception as e:
                print(f"Error sending CALIBRATION command: {e}")
        else:
            print("Serial connection not open.")

        # Close the popup window after sending the 'a' character
        self.root.focus_set()  
        self.calibrate_window.destroy()

    def request_translation(self):
        if hasattr(self, 'serial_connection') and self.serial_connection.is_open:
            try:
                self.serial_connection.write(b'c')  
                time.sleep(0.02)
                self.serial_connection.write(self.spinbox2.get().encode('utf-8'))
                print("Move requested")
            except Exception as e:
                print(f"Error sending MOVE command: {e}")
        else:
            print("Serial connection not open.")


    def on_start_click(self):
        if self.start_state:
            self.stop();
        else:
            self.button3.config(text="Stop")
            self.start_state = True
            self.request_oscillation()
            self.monitor_oscillation()
            self.stop()

    def stop(self):
        self.button3.config(text="Start")
        self.start_state = False


    def request_oscillation(self):
        if hasattr(self, 'serial_connection') and self.serial_connection.is_open:
            try:
                self.serial_connection.write(b'd')  
                time.sleep(0.02)
                self.serial_connection.write(self.spinbox1.get().encode('utf-8'))
                time.sleep(0.02)
                self.serial_connection.write(self.spinbox3.get().encode('utf-8'))
                time.sleep(0.02)
                self.serial_connection.write(self.spinbox4.get().encode('utf-8'))
                print("Oscillation requested")
            except Exception as e:
                print(f"Error sending MOVE command: {e}")
        else:
            print("Serial connection not open.")

    def monitor_oscillation(self):
        self.serial_connection.flushInput()
        while True:
            if self.serial_connection.in_waiting > 0:
                cycle = self.serial_connection.readline().decode('utf-8').strip()
                print("N°:", cycle)
                cycle = int(cycle)
                if cycle >= int(self.spinbox1.get()) or cycle < 0:
                    return




root = tk.Tk()
strain_gui = StrainGui(root)
root.mainloop()
 
