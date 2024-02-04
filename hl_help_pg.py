import tkinter as tk 
from PIL import Image, ImageTk

mw = tk.Tk()
mw.config(bg = "#FFE4C4")
mw.title("Help Page")

def next_pg():
    mw.destroy()
    import hl_single_spring
    
l1 = tk.Label(mw, text = "Below is a brief instruction on how to navigate around the Hooke's Law Simulator. \nKindly click into the 'Help' Button in the main page if confusion arises", bg = "#FFE4C4", justify= tk.LEFT, font = ("helvetica", 15)).grid(row = 0, sticky="W", padx=20, pady=10)

im = Image.open("Help Button Pic.png")
photo = ImageTk.PhotoImage(im)

bg = tk.Label(image = photo)
bg.image = photo
bg.grid(row = 1, padx=20)

next_btn = tk.Button(mw, width = 10, font=("Arial Black", 10), text="NEXT", command=next_pg).grid(row=2, sticky="E", padx=20, pady=10)

mw.mainloop()
