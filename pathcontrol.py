
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog


class PathControl(ttk.Frame):
    def __init__(self, master, text, textvariable=None):
        super().__init__(master, style='PathControl.TFrame')

        if textvariable is None:
            textvariable = tk.StringVar(self)
        
        self._var = textvariable

        pad = {'padx': 2, 'pady': 2}

        ttk.Label(self, text=text).pack(side=tk.LEFT, **pad)
        ttk.Entry(self, textvariable=self._var).pack(side=tk.LEFT, fill=tk.X, expand=True, **pad)
        ttk.Button(self, text='...', command=self._action, width=3).pack(side=tk.RIGHT, **pad)
    
    def _action(self):
        filename = filedialog.askopenfilename(parent=self, filetypes=[('RLMMS Data', '*.txt'), ('All Files', '*.*')])
        if filename:
            self._var.set(filename)


