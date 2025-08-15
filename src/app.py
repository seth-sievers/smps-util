import tkinter as tk 
from tkinter import ttk
import sv_ttk 

# this class owns the application, it will be blocking
class App():
        def __init__(self):
                self.root = tk.Tk() # main application GUI object 
                self.root.title('SMPS UTIL') # Title of the application window 
                sv_ttk.set_theme('light') # Custom theme settings
                # MainWindow(self.root).pack() 

        pass




# def run_gui():
#         return 

# allow for testing the GUI by running it solo 
# def main():
#         run_gui()
#         return

# if __name__ == '__main__':
#         main()