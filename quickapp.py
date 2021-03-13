
import tkinter as tk
import tkinter.ttk as ttk


def quickapp(cls, title='tk'):
    root = tk.Tk()
    root.title(title)
    cls(root).pack(expand=True, fill=tk.BOTH)
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    root.mainloop()
