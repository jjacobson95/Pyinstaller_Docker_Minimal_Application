
from time import sleep
import tkinter as tk
import tkinter.filedialog
from tkinter.ttk import *
from tkinter import ttk
from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter.messagebox import askyesno
from tkinter import messagebox as msg
from tkinter import font
import os
import threading
from ttkthemes import ThemedTk
import json
import platform
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.lines import Line2D
from tkPDFViewer import tkPDFViewer as pdf
import multiprocessing
import Run_docker

if __name__=="__main__":
    print("name is main")
    #This may be needed for pyinstaller.
    multiprocessing.freeze_support()
    #Set working directory
    cur_dir = os.path.dirname(__file__)
    os.chdir(cur_dir)
    # Initialize application     
    window = ThemedTk(theme="none")
    window.title("Dashboard of Failure",)
    window.config(bg='#0C74BA')

    def run_docker():
        all_results = Run_docker.run_container()


    Mode_Frame = LabelFrame(window)
    Mode_Frame.grid(row=1, column = 0, sticky="NSWE")
    Mode_Frame.grid_columnconfigure(0, weight=1)
    Mode_buttons = Button(Mode_Frame, text = "This is a Button. It will call Run_docker.py. Within Run_docker.py, a 3 containers will be spun up from a docker image and exec_run will be used.", height = 40, width = 120,bg='lightgrey', command=lambda:[run_docker()])
    Mode_buttons.grid(row=0, column = 0, sticky="NEWS")

    window.mainloop()
