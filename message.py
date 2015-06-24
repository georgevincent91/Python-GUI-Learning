from Tkinter import *

root = Tk()
explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface
exists to allow additional image file
formats to be added easily."""
w = Label(root,
          compound = CENTER,
          text=explanation,
          ).pack(side="right")

root.mainloop()