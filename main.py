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
import csv 


###############################################################################
#                                  CONSTANTS                                  #
###############################################################################

# Paths
DATA_FILE_PATH = "data/radiation_exemples.csv"
ENCODING = "utf-8"

# Window
WINDOW_TITLE = "RadConvert"
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 300

# UI
UI_FONT = ("Arial", 12)
UI_PADDING_Y = 10
UI_PADDING_X = 20

# TEXT
TEXT_TITLE = "RadConvert"
TEXT_DESCRIPTION = "This project converts and compares real life exemple of radiation units using XKCD's radiation chart (https://xkcd.com/radiation/)"
TEXT_BUTTON_CLOSE = "Close"


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
    result = None
    try:
        result = value * values_dict[unit_from] / values_dict[unit_to] 
    except Exception as e:
        print(f"Error: {e}")
    return result


###############################################################################
#                                    MAIN                                     #
###############################################################################

def main(debug = False):
    """
    Create the main window of the program
    """

    if debug: print("\nBEGIN RadConvert/main.py")

    # Load the units from the radiation_exemples.csv file
    # get the keys of the dictionary as a list
    ALL_UNITS = list(load_units(DATA_FILE_PATH).keys())

    # Display a window
    root = tk.Tk()
    root.title(WINDOW_TITLE)
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    # Display the title of the window as a label
    title = tk.Label(root, text=TEXT_TITLE, font=UI_FONT)
    
    # Display the description of the window as a label.
    # Must be a multi-line text
    description = tk.Label(
        root,
        text=TEXT_DESCRIPTION,
        font=UI_FONT,
        wraplength=WINDOW_WIDTH
    )


    # DISPLAY THE UNIT CONVERTER
    # Two entry fields to input the value and the unit
    # A dropdown menu to select the unit to convert to under each entry field
    # The converted value is displayed in the other entry field

        # Display the two entry fields side by side
        # Put them in a frame
        # Add a dropdown menu under each entry field
        # Display the converted value in the other entry field
    
    # Frames
    entry_frame = tk.LabelFrame(root, text="Unit converter")

    entry_1_frame = tk.Frame(entry_frame)
    entry_2_frame = tk.Frame(entry_frame)
    
    # Vars
    entry_value_1_var = tk.StringVar()
    entry_value_2_var = tk.StringVar()
    entry_dropdown_1_var = tk.StringVar()
    entry_dropdown_2_var = tk.StringVar()

    # Widgets
    entry_value_1 = tk.Entry(entry_1_frame, font=UI_FONT, textvariable=entry_value_1_var)
    entry_value_2 = tk.Entry(entry_2_frame, font=UI_FONT, textvariable=entry_value_2_var)
    
    entry_dropdown_1 = tk.OptionMenu(entry_1_frame, entry_dropdown_1_var, *ALL_UNITS)
    entry_dropdown_2 = tk.OptionMenu(entry_2_frame, entry_dropdown_2_var, *ALL_UNITS)
    entry_dropdown_1_var.set(ALL_UNITS[0])
    entry_dropdown_2_var.set(ALL_UNITS[0])

    button_close = tk.Button(
        root,
        text=TEXT_BUTTON_CLOSE,
        font=UI_FONT,
        command=root.quit
    )

    # Trace the entry fields
    def trace_entry_1(*args):
        try:
            value = float(entry_value_1_var.get())
            unit_from = entry_dropdown_1.cget("text")
            unit_to = entry_dropdown_2.cget("text")
            result = convert(value, unit_from, unit_to, load_units(DATA_FILE_PATH))
            entry_value_2_var.set(result)
        except ValueError:
            entry_value_2_var.set("")

    def trace_entry_2(*args):
        try:
            value = float(entry_value_2_var.get())
            unit_from = entry_dropdown_2.cget("text")
            unit_to = entry_dropdown_1.cget("text")
            result = convert(value, unit_from, unit_to, load_units(DATA_FILE_PATH))
            entry_value_1_var.set(result)
        except ValueError:
            entry_value_1_var.set("")

    # Trace the dropdown menus

    entry_value_1_var.trace("w", trace_entry_1)
    entry_value_2_var.trace("w", trace_entry_2)
    entry_dropdown_1_var.trace("w", trace_entry_1)
    entry_dropdown_2_var.trace("w", trace_entry_2)
    
    
    # PACK ALL THE WIDGETS
    # Title & Description
    title.pack(pady=UI_PADDING_Y)
    description.pack(pady=UI_PADDING_Y)
    
    # Entry fields side by side but sticking to each other
    entry_value_1.pack(side=tk.TOP, pady=UI_PADDING_Y, padx=UI_PADDING_X)
    entry_value_2.pack(side=tk.TOP, pady=UI_PADDING_Y, padx=UI_PADDING_X)

    entry_dropdown_1.pack(side=tk.TOP, pady=UI_PADDING_Y, padx=UI_PADDING_X)
    entry_dropdown_2.pack(side=tk.TOP, pady=UI_PADDING_Y, padx=UI_PADDING_X)

    entry_1_frame.pack(side=tk.LEFT, pady=UI_PADDING_Y)
    entry_2_frame.pack(side=tk.LEFT, pady=UI_PADDING_Y)

    entry_frame.pack(pady=UI_PADDING_Y)


    # Close button
    button_close.pack(pady=UI_PADDING_Y)

    # Main loop
    root.mainloop()
    
    if debug: print("\nEND")


if __name__ == "__main__":
    main(debug=False)