# tkutils-py

A collection of utilities for tkinter and ttk.


## Usage

### Git Submodule

```sh
git submodule add https://gitlab.com/twh2898/tkutils.git
```


### Install

```sh
git clone https://gitlab.com/twh2898/tkutils.git
cd tkutils
pip install --user .
```


### Developer Install

A developer install will link to the project code rather than copying the code
into the system. This allows you to update the code without having to install
again.

```sh
git clone https://gitlab.com/twh2898/tkutils.git
cd tkutils
pip install --user -e .
```


## API

### PathControl

```py
from tkutils import tk, ttk, PathControl

root = tk.Tk()
f = ttk.Frame(root)
f.pack()
var = tk.StringVar()
filetypes = [
    ('Text File', '*.txt'),
    ('CSV File', '*.csv'),
    ('TSV File', '*.txt'),
    ('TSV File', '*.xlm'),
    ('All Files', '*.*')
]
PathControl(f, 'File Path', textvariable=var, title='Open File', filetypes=filetypes).pack()
root.mainloop()
```

### quickapp

```py
from tkutils import tk, ttk, quickapp

class App(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        ttk.Label(self, text='Hello World').pack()

if __name__ == '__main__':
    quickapp(App, 'quickapp Demo')
```

### validate_float, validate_int

```py
from tkutils import tk, ttk, validate_float, validate_int

root = tk.Tk()
f = ttk.Frame(root)
f.pack()
vcmd = (root.register(validate_float), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
var = tk.DoubleVar()
ttk.Entry(f, validate='key', validatecommand=vcmd, textvariable=var).pack()
root.mainloop()
```

### VerticalScrolledFrame

The code for `VerticalScrolledFrame` is adapted from
http://tkinter.unpythonic.net/wiki/VerticalScrolledFrame

This widget is intended for scrolling a Frame. For widgets like `Listbox` or `Text` use the
"regular" scrollbar code.

```py
from tkutils import tk, ttk, VerticalScrolledFrame

root = tk.Tk()
f = VerticalScrolledFrame(root)
f.pack()
for i in range(10):
    ttk.Button(f.interior, text='Button ' + str(i)).pack()

root.mainloop()
```

