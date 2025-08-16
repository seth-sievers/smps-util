import tkinter as tk 
from tkinter import ttk
import tkinter.font as tkFont
import sv_ttk 
from converter import Converter
import buck

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
                self.columnconfigure(0, weight=1, uniform='group1') # LeftColumn
                self.columnconfigure(1, weight=1, uniform='group1') # MiddleColumn
                self.columnconfigure(2, weight=1, uniform='group1') # Right Column 
                self.rowconfigure(0, weight=1) # allow resizing 

                # add LeftColumn into its grid 
                LeftColumn(self).grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

                # add placeholder empty frames so that the middle and right columns do not collapse 
                #MiddleColumn(self).grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
                #RightColumn(self).grid(row=0, column=2, padx=10, pady=10, sticky='nsew')

class LeftColumn(ttk.Frame):
        def __init__(self, parent):
                super().__init__(parent, padding=15)

                # setup n x 1 grid 
                self.rowconfigure(0, weight=0) # ConverterTypeComboBox, fixed height 
                self.rowconfigure(1, weight=1)
                self.columnconfigure(0, weight=1) # allow resizing 

                # add ConverterTypeLabelBox LabelFrame into its grid 
                ConverterTypeComboBox(self).grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

# need to put a blank frame in the main window columns so it does not collapse to minimal size
class MiddleColumn(ttk.Frame):
        def __init__(self, parent):
                super().__init__(parent, padding=15)

# need to put a blank frame in the main window columns so it does not collapse to minimal size
class RightColumn(ttk.Frame):
        def __init__(self, parent):
                super().__init__(parent, padding=15)

class ConverterTypeComboBox(ttk.LabelFrame):
        def __init__(self, parent):
                # change the fontsize
                style = ttk.Style()
                style.configure('ComboBoxFrame.TLabelframe', padding=10)
                style.configure('ComboBoxFrame.TLabelframe.Label', font=("Arial", 12))

                super().__init__(parent, text='Topology', padding=30, style='ComboBoxFrame.TLabelframe')

                # create the Converter Type Select Box 
                self.converter_select_box = ttk.Combobox(self, state='readonly')

                # update the entries of the box 
                combo_values = [x.topology for x in Converter().converter_list]
                self.converter_select_box['values'] = combo_values
                self.converter_select_box.current(0)

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