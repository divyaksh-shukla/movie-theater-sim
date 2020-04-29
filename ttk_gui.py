import tkinter as tk
from tkinter import font as font
import imp
import sys
import os
# movie_theater = imp.load_compiled("movie_theater", os.path.join(os.getcwd(), "movie_theatre.cpython-35.pyc"))
# run_simulation = movie_theater.run_simulation
from movie_theatre import run_simulation
# from tkinter import ttk

def create_widgets(root):
    configure_grid(root)

    heading_label = tk.Label(root)
    heading_label.configure(text = "Movie Theater Simulator", font = "Arial 18", pady = 10)
    heading_label.grid(row = 1, column = 1, columnspan = 2)
    # heading_label.pack(anchor = "center")

    cashiers_label = tk.Label(root, text = "No. of Cashiers")
    cashiers_label.configure(font = "Arial 11", padx = 10)

    servers_label = tk.Label(root, text = "No. of Servers")
    servers_label.configure(font = "Arial 11", padx = 10)

    ushers_label = tk.Label(root, text = "No. of Ushers")
    ushers_label.configure(font = "Arial 11", padx = 10)

    cashiers_entry = tk.Entry(root)
    servers_entry = tk.Entry(root)
    ushers_entry = tk.Entry(root)

    simulate_button = tk.Button(root, text="Simulate", command = lambda: do_simulation(cashiers_entry.get(), servers_entry.get(), ushers_entry.get()))
    simulate_button.configure(font = "Arial 14")

    cashiers_label.grid(row = 2, column = 1, sticky="e")
    cashiers_entry.grid(row = 2, column = 2, sticky="w")
    servers_label.grid(row = 3, column = 1, sticky="e")
    servers_entry.grid(row = 3, column = 2, sticky="w")
    ushers_label.grid(row = 4, column = 1, sticky="e")
    ushers_entry.grid(row = 4, column = 2, sticky="w")
    simulate_button.grid(row = 5, column = 1, columnspan = 2, sticky = "ew", pady = 20)

    def do_simulation(num_cashiers, num_servers, num_ushers):
        mins, secs = run_simulation(int(num_cashiers), int(num_servers), int(num_ushers))
        result_label = tk.Label(root, text="The average wait time is {} minutes and {} seconds.".format(mins, secs), font="Arial 11")
        result_label.grid(row = 6, column = 0, columnspan = 4)

def get_screen_width_height(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    return screen_width, screen_height

def center(root, width, height):
    screen_width, screen_height = get_screen_width_height(root)
    root.geometry("+{}+{}".format(int(screen_width/2-width/2), int(screen_height/2-height/2)))

def create_window(root, width, height):
    root.wm_minsize(width=width, height=height)
    # root.geometry("{}x{}".format(int(width), int(height)))
    root.wm_title("Movie Theater Simulator")

def configure_grid(root):
    root.grid_columnconfigure(index=0, weight=1)
    root.grid_columnconfigure(index=1, weight=1)
    root.grid_columnconfigure(index=2, weight=1)
    root.grid_columnconfigure(index=3, weight=1)
    root.grid_columnconfigure(index=4, weight=1)
    root.grid_rowconfigure(index=0, weight=1)
    root.grid_rowconfigure(index=1, weight=1)
    root.grid_rowconfigure(index=2, weight=1)
    root.grid_rowconfigure(index=3, weight=1)
    root.grid_rowconfigure(index=4, weight=1)
    root.grid_rowconfigure(index=5, weight=1)
    root.grid_rowconfigure(index=6, weight=1)

def main():
    root = tk.Tk()
    width = 400
    height = 100
    main_container = tk.Frame(root)
    main_container.pack()
    create_window(root, width=width, height=height)
    center(root, width=width, height=height)
    create_widgets(main_container)
    create_window(root, width if (root.winfo_reqwidth() < width) else root.winfo_reqwidth(), root.winfo_reqheight())
    root.mainloop()

main()