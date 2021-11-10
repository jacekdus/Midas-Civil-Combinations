from tkinter import *

from tkinter import ttk


def clicked():
    # lbl.configure(text="Button was clicked !!")
    print('button clicked!')


class GUI:
    def __init__(self):
        window = Tk()

        window.title("Midas-Civil-Combinations")
        window.geometry('500x500')

        tab_control = ttk.Notebook(window)

        # Tabs
        tab_load_case = ttk.Frame(tab_control)
        tab_combinations = ttk.Frame(tab_control)
        tab_config = ttk.Frame(tab_control)

        # Load Cases Tab
        tab_control.add(tab_load_case, text='Przypadki')
        load_case_tab_label = Label(tab_load_case, text='Lista przypadków', anchor='w')
        load_case_tab_listbox = Listbox(tab_load_case)
        load_case_input_label = Label(tab_load_case, text="Load Case: ")  # Input
        load_case_add_input = Entry(tab_load_case, width=10)
        load_case_add_submit_button = Button(tab_load_case, text="Submit", command=clicked)

        load_case_tab_label.pack(side=LEFT)
        load_case_tab_listbox.pack(side=LEFT)
        load_case_input_label.pack(side=LEFT)
        load_case_add_input.pack(side=LEFT)
        load_case_add_submit_button.pack(side=LEFT)

        # # Load Combinations Tab
        # tab_control.add(tab_combinations, text='Kombinacje')
        # lbl2 = Label(tab_combinations, text= 'Lista kombinacji', anchor='w')
        # lb_load_comb = Listbox(tab_combinations)
        # lb_load_comb.grid(column=0, row=1)
        # lb_load_comb = Listbox(tab_combinations)
        # lb_load_comb.grid(column=1, row=1)
        # lbl2.grid(column=0, row=0)
        #
        # # Config Tab
        # tab_control.add(tab_config, text='Opcje')
        # mct_chk = Checkbutton(tab_config, text='Stwórz MCT Command', anchor='w')
        # log_chk = Checkbutton(tab_config, text='Stwórz Log', anchor='w')
        # mct_chk.pack(fill='both')
        # log_chk.pack(fill='both')

        # btn = Button(window, text="Click Me")

        tab_control.pack(expand=1, fill='both')

        window.mainloop()

