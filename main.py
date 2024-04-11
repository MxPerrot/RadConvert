# -*- encoding: utf-8 -*-
# 
# Author: @MxPerrot <mailto:maxime.perrot10@univ-rennes.fr>
# GitHub: MxPerrot/RadConvert
# Created: 2024-04-09
# Python: 3.12.2
# 
# Description: Main file of the RadConvert program
# This project converts and compares real life exemple of radiation units using
# XKCD's radiation chart (https://xkcd.com/radiation/)
# It uses a tkinter GUI to display the user interface


###############################################################################
#                                   IMPORTS                                   #
###############################################################################

import tkinter as tk
import tkinter.ttk as ttk
import csv 


###############################################################################
#                                  CONSTANTS                                  #
###############################################################################

# Debug
DEBUG = False

# Paths
DATA_FILE_PATH = "data/radiation_exemples.csv"
ENCODING = "utf-8"

# Window
WINDOW_TITLE = "RadConvert"
WINDOW_MIN_WIDTH = 500
WINDOW_MIN_HEIGHT = 300
WINDOW_WIDTH = WINDOW_MIN_WIDTH
WINDOW_HEIGHT = WINDOW_MIN_HEIGHT

# UI
UI_FONT = ("Arial", 12)
UI_PADDING_Y = 10
UI_PADDING_X = 20

# TEXT
TEXT_TITLE = "RadConvert"
TEXT_DESCRIPTION = "This project converts and compares real life exemple of radiation units using XKCD's radiation chart (https://xkcd.com/radiation/)"
TEXT_SWAP_BUTTON = "⇄"
ENTRY_FRAME_TITLE = "Unit Converter"

# TKINTER
CENTER = "center"
LEFT = "left"
RIGHT = "right"
WRITE = "w"
READ_ONLY = "readonly"

###############################################################################
#                                  FUNCTIONS                                  #
###############################################################################

def load_units(data_file_path):
    """
    Load the units from the radiation_exemples.csv file : "unit", value in Sv
    Return a dictionary with the unit as key and the value in Sv as value
    """
    units = {}
    with open(data_file_path, "r", encoding=ENCODING) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            units[row[0]] = float(row[1])
    return units

def convert(value, unit_from, unit_to, values_dict):
    """
    Convert a value from one unit to another
    """
    result = value * values_dict[unit_from] / values_dict[unit_to]
    if DEBUG: print(f"Converted {value} {unit_from} to {result} {unit_to}")
    return result

def swap_units(menu_1, menu_2):
    """
    Swap the units in the combobox menus
    """
    if DEBUG: print("Swapping units")
    
    # Get the current values
    value_1 = menu_1.get()
    value_2 = menu_2.get()
    if DEBUG: print(f"Value 1: {value_1}, Value 2: {value_2}")
    
    # Set the swapped values
    menu_1.set(value_2)
    menu_2.set(value_1)
    if DEBUG: print("Set the swapped values")
    

###############################################################################
#                                    MAIN                                     #
###############################################################################

def main():
    """
    Create the main window of the program
    """

    if DEBUG: print("\nBEGIN RadConvert/main.py")


    #############
    # CONSTANTS #
    #############

    # Load the units from the radiation_exemples.csv file
    # get the keys of the dictionary as a list
    ALL_UNITS = list(load_units(DATA_FILE_PATH).keys())


    ##########
    # WINDOW #
    ##########

    # Display a window
    root = tk.Tk()
    root.title(WINDOW_TITLE)
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    root.minsize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)

    # Vars
    entry_value_1_var    = tk.StringVar()
    entry_value_2_var    = tk.StringVar()
    entry_combobox_1_var = tk.StringVar()
    entry_combobox_2_var = tk.StringVar()


    ###########
    # WIDGETS #
    ###########

    # Frames
    entry_frame   = tk.LabelFrame(root,text=ENTRY_FRAME_TITLE)
    entry_1_frame = tk.Frame(entry_frame)
    entry_2_frame = tk.Frame(entry_frame)
    
    # Title
    title = tk.Label(root,text=TEXT_TITLE,font=UI_FONT)
    
    # Description
    description = tk.Label(root,text=TEXT_DESCRIPTION,font=UI_FONT,wraplength=WINDOW_WIDTH)

    # Entry fields
    entry_value_1 = tk.Entry(entry_1_frame,font=UI_FONT,textvariable=entry_value_1_var)
    entry_value_2 = tk.Entry(entry_2_frame,font=UI_FONT,textvariable=entry_value_2_var)
    
    # Swap button
    swap_button = tk.Button(entry_frame,text=TEXT_SWAP_BUTTON,command=lambda: swap_units(entry_combobox_1, entry_combobox_2))

    # Dropdown menus
    entry_combobox_1 = ttk.Combobox(entry_1_frame,state=READ_ONLY,values=ALL_UNITS,textvariable=entry_combobox_1_var)
    entry_combobox_2 = ttk.Combobox(entry_2_frame,state=READ_ONLY,values=ALL_UNITS,textvariable=entry_combobox_2_var)
    
    # Set the default values of the dropdown menus
    entry_combobox_1.set(ALL_UNITS[0])
    entry_combobox_2.set(ALL_UNITS[0])

    # Trace the entry fields
    def trace_entry_1(*args):
        try:
            value = float(entry_value_1_var.get())
            unit_from = entry_combobox_1_var.get()
            unit_to = entry_combobox_2_var.get()
            result = convert(value, unit_from, unit_to, load_units(DATA_FILE_PATH))
            entry_value_2_var.set(result)
        except ValueError:
            entry_value_2_var.set("")

    def trace_entry_2(*args):
        try:
            value = float(entry_value_2_var.get())
            unit_from = entry_combobox_2_var.get()
            unit_to = entry_combobox_1_var.get()
            result = convert(value, unit_from, unit_to, load_units(DATA_FILE_PATH))
            entry_value_1_var.set(result)
        except ValueError:
            entry_value_1_var.set("")
    
    # Trace the dropdown menus
    entry_value_1_var.trace(WRITE, trace_entry_1)
    entry_value_2_var.trace(WRITE, trace_entry_2)
    entry_combobox_1_var.trace(WRITE, trace_entry_1)
    entry_combobox_2_var.trace(WRITE, trace_entry_1) # trace_entry_1 because the left entry field is the fixed input, while the right one is the output
    
    ###########
    # PACKING #
    ###########

    # Title
    title.pack(pady=UI_PADDING_Y)
    
    # Description
    description.pack(pady=UI_PADDING_Y)
    
    # Entry fields side by side but sticking to each other with swap button in the middle
    entry_value_1.pack(side=tk.TOP, pady=UI_PADDING_Y, padx=UI_PADDING_X)
    swap_button.place(relx=0.5, rely=0.31, anchor=CENTER)
    entry_value_2.pack(side=tk.TOP, pady=UI_PADDING_Y, padx=UI_PADDING_X)

    # Dropdown menus side by side
    entry_combobox_1.pack(side=tk.TOP, pady=UI_PADDING_Y, padx=UI_PADDING_X)
    entry_combobox_2.pack(side=tk.TOP, pady=UI_PADDING_Y, padx=UI_PADDING_X)

    # Frames
    entry_1_frame.pack(side=tk.LEFT, pady=UI_PADDING_Y)
    entry_2_frame.pack(side=tk.LEFT, pady=UI_PADDING_Y)
    entry_frame.pack(pady=UI_PADDING_Y)

    # Main loop
    root.mainloop()
    
    if DEBUG: print("\nEND")


if __name__ == "__main__":
    main()