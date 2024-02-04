import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance

mw = tk.Tk()
mw.config(width = 800, bg = "#FFE4C4")


bg_img = Image.open("spring.jpg")

enhancer = ImageEnhance.Brightness(bg_img)

factor = 0.5
bg_output = enhancer.enhance(factor)
bg_output.save("darkened_bg.jpg")

darkened_bg = Image.open("darkened_bg.jpg")
resized_bg = darkened_bg.resize((1500, 500), Image.ANTIALIAS)

bg_pic = ImageTk.PhotoImage(resized_bg)
bg_ = tk.Label(image = bg_pic)
bg_.image = bg_pic
bg_.grid(rowspan=3)

def split_text(text):
    words = text.split()
    split_text = ""
    count = 0
    for word in words:
        split_text += word + " "
        count += 1
        if count == 15:
            split_text += "\n"
            count = 0
    return split_text

title_1 = tk.Label(mw, width = 40, text = "WELCOME TO HOOKE'S LAW SIMULATOR", font = ("arial black", 35), bg='#FFE4C4').grid(row = 0)

intro_para = "The program would allow students to input different variables such as force, displacement, and the spring constant, and see the resulting changes in the spring's behaviour. Besides, the program could also provide real-time feedback and visualisations to help students understand the concepts. For example, students could adjust the spring constant and see how it affects the behaviour of the spring when force is applied, or they could input different levels of force and see how the spring responds. Furthermore, the program should also include interactive elements such as sliders, buttons, and graphs to make the learning experiene more engaging and informative."
intro_para = split_text(intro_para)
intro = tk.Label(mw, font = ("helvetica", 20), text = intro_para, bg='#FFE4C4').grid(row = 1)

def next_pg():
    mw.destroy()
    import hl_help_pg

next_btn = tk.Button(mw, width = 10, font=("Arial Black", 10), text="NEXT", command=next_pg).grid(row=2, sticky="E", padx=45)
mw.mainloop()