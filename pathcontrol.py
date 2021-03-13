
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog


class PathControl(ttk.Frame):
    def __init__(self, master, label, textvariable=None, title='Open File', filetypes=[('All Files', '*.*')], style='PathControl.TFrame'):
        super().__init__(master, style=style)

        if textvariable is None:
            textvariable = tk.StringVar(self)

        self._var = textvariable
        self._title = title
        self._filetypes = filetypes

        pad = {'padx': 2, 'pady': 2}

        ttk.Label(self, text=label).pack(side=tk.LEFT, **pad)
        ttk.Entry(self, textvariable=self._var).pack(
            side=tk.LEFT, fill=tk.X, expand=True, **pad)
        ttk.Button(self, text='...', command=self._action,
                   width=3).pack(side=tk.RIGHT, **pad)

    def get(self):
        return self._var.get()

    def _action(self):
        filename = filedialog.askopenfilename(
            parent=self, title=self._title, filetypes=self._filetypes)
        if filename:
            self._var.set(filename)
