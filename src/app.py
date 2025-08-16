import tkinter as tk 
from tkinter import ttk
import tkinter.font as tkFont
import sv_ttk 

# this class owns the application, it will be blocking
class App():
        def __init__(self):
                self.root = tk.Tk() # main application GUI object 
                self.root.title('SMPS Utility') # Title of the application window 
                sv_ttk.set_theme('light') # Custom theme settings
                MainWindow(self.root).pack(expand=True, fill = 'both') # Put the main window frame in the application 
        def run(self):
                # blocking application loop
                self.root.mainloop()
                return

class MainWindow(ttk.Frame):
        def __init__(self, parent):
                super().__init__(parent, padding=15)

                # setup a 1x3 (1 tall, 3 wide) grid to organize the elements
                self.columnconfigure(0, weight=1) # LeftColumn
                self.columnconfigure(1, weight=1) # MiddleColumn
                self.columnconfigure(2, weight=1) # Right Column 
                self.rowconfigure(0, weight=1) # allow resizing 

                # add LeftColumn into its grid 
                LeftColumn(self).grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

class LeftColumn(ttk.Frame):
        def __init__(self, parent):
                super().__init__(parent, padding=15)

                # setup n x 1 grid 
                self.rowconfigure(0, weight=0) # ConverterTypeComboBox, fixed height 
                self.rowconfigure(1, weight=1)
                self.columnconfigure(0, weight=1) # allow resizing 

                # add ConverterTypeLabelBox LabelFrame into its grid 
                ConverterTypeComboBox(self).grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

class ConverterTypeComboBox(ttk.LabelFrame):
        def __init__(self, parent):
                super().__init__(parent, text="Topology",padding=30)

                # create the Converter Type Select Box 
                self.converter_select_box = ttk.Combobox(self, state='readonly')

                # pack the select box into the frame 
                self.converter_select_box.pack(expand=True, fill='both')




# def run_gui():
#         return 

# allow for testing the GUI by running it solo 
# def main():
#         run_gui()
#         return

# if __name__ == '__main__':
#         main()