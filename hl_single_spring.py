import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import math

mw = tk.Tk(className = "Hooke's Law Experiment")
mw.configure(bg = "#FFE4C4")

####################################################################################
##define the function to resize the image
def resize_image(force_1, extension_1, force_2, extension_2):
    global image_spring, tk_image_spring
    # Convert the new_width argument to an integer
    new_spring_width = image_spring.width + int(force_1) - int(force_2) + int(extension_1) + int(extension_2)
    new_spring_height = image_spring.height
    # Resize the image with the new width and height
    resized_image = image_spring.resize((new_spring_width, new_spring_height))
    # Create a new PhotoImage from the resized image
    tk_image_spring = ImageTk.PhotoImage(resized_image)
    # Update the canvas image with the new PhotoImage
    spring.itemconfig(spring_image, image=tk_image_spring, anchor='w')
    spring.coords(spring_image, -10, 170)

####################################################################################
##inserting canvas on tkinter screen
wall = tk.Canvas(mw, width = 160, height = 330, bg = "white")
wall.grid(row = 1, column = 0)

spring = tk.Canvas(mw, width = 652, height = 330, bg = "white")
spring.grid(row = 1, column = 1, columnspan = 4)

graph = tk.Canvas(mw, width = 500, height = 500, bg = "white")
graph.grid(row = 1, column = 5, rowspan = 5)

x_graph = tk.Canvas(mw, width = 500, height = 500, bg = "white")


###################################################################################
##Create spring animation
# Open the image file and create a PhotoImage
image_wall = Image.open(r"wall.png")
image_spring = Image.open(r"single spring.png")

# Convert the image to a Tkinter PhotoImage
tk_image_wall = ImageTk.PhotoImage(image_wall)
tk_image_spring = ImageTk.PhotoImage(image_spring)

# Add the Tkinter PhotoImage to the canvas at centre
wall.create_image(130, 170, image=tk_image_wall)
spring_image = spring.create_image(280, 170, image=tk_image_spring)

####################################################################################
##intro button msgbox functions
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

def introduction_click():
    intro_box = tk.Toplevel(mw, bg="#ADD8E6")
    intro_box.title("Mode Choices")

    intro_title_label = tk.Label(intro_box, text = "INTRODUCTION", bg="#ADD8E6", font = ("arial black", 20)).grid(row = 0, pady=10)

    intro_text = "Hooke's Law is a fundamental physics concept that describes the relationship between a force applied to an elastic material and the resulting deformation or displacement. The program would allow students to input different variables, such as force, displacement, and the spring constant, and see the resulting changes in the spring's behaviour. Besides, the program could also provide real-time feedback and visualisations to help students better understand the concepts. For example, students could adjust the spring constant and see how it affects the behavior of the spring when force is applied, or they could input different levels of force and see how the spring responds."
    intro_text = split_text(intro_text)
    intro_label = tk.Label(intro_box, text=intro_text, bg="#ADD8E6", font=("Helvetica", 15)).grid(row=1, padx=20)

    # Add close button functionality
    intro_box.protocol("WM_DELETE_WINDOW", intro_box.destroy) 
    ok_btn = tk.Button(intro_box, width = 10, font=("Arial Black", 10), text="OK", command=intro_box.destroy).grid(row=2, sticky="E", padx=20, pady=10)
    intro_box.mainloop()

#####################################################################
##theory button msgbox functions
def theory_click():
    theo_box = tk.Toplevel(mw, bg="#ADD8E6")
    theo_box.title("Theory")

    theo_title_label = tk.Label(theo_box, text = "THEORY", bg="#ADD8E6", font = ("arial black", 20)).grid(row = 0, pady=10)
    
    theo_text = "Hooke’s Law states that the extension of a spring is directly proportional to the force applied to the spring, given that the elastic limit of the spring is not exceeded (phys.org, 2015). With this equation F = -kx where F is the force applied to the string, x is the spring extension and k is the spring constant (Robert Hooke, 1678). To add to that '-x' is a negative value demonstrating that the spring's displacement, once it is stretched. 'k', is the spring constant and it shows the stiffness of the spring. The value of Elastic Potential Energy is represented by the area under the graph and can be calculated using formula EPE = 1/2 Fx or EPE = 1/2kx^2"
    theo_text = split_text(theo_text)
    theo_label = tk.Label(theo_box, text=theo_text, bg="#ADD8E6", font=("Helvetica", 15)).grid(row=1, padx=20)

    # Add close button functionality
    theo_box.protocol("WM_DELETE_WINDOW", theo_box.destroy) 
    ok_btn = tk.Button(theo_box, width = 10, font=("Arial Black", 10), text="OK", command=theo_box.destroy).grid(row=2, sticky="E", padx=20, pady=10)
    theo_box.mainloop()

#######################################################################
##simulation button msgbox functions
def simulation_click():
    sim_box = tk.Toplevel(mw, bg="#ADD8E6")
    sim_box.title("Mode Choices")
    
    pic_1 = Image.open("single spring.png")
    pic_1 = pic_1.resize((298, 200), Image.ANTIALIAS)
    sis_pic = ImageTk.PhotoImage(pic_1)
    
    pic_2 = Image.open("parallel spring.png")
    pic_2 = pic_2.resize((298, 200), Image.ANTIALIAS)
    sps_pic = ImageTk.PhotoImage(pic_2)
    
    pic_3 = Image.open("series spring.png")
    pic_3 = pic_3.resize((298, 200), Image.ANTIALIAS)
    ses_pic = ImageTk.PhotoImage(pic_3)
    
    def single_win():
        sim_box.destroy()
        mw.destroy()
        import hl_single_spring
        sim_box.update()
        
    def series_win():
        sim_box.destroy()
        mw.destroy()
        import hl_spring_parallel
        sim_box.update()
        
    def parallel_win():
        sim_box.destroy()
        mw.destroy()
        import hl_spring_series
        sim_box.update()
    
    sim_label = tk.Label(sim_box, text = "CHOOSE ONE OF THE SIMULATOR", width=56, bg="#ADD8E6", font = ("arial black", 20)).grid(row = 0, columnspan = 3, pady=10)
    
    sis_label = tk.Label(sim_box, text = "Single Spring", width=27, bg="white", font = ("arial black", 12)).grid(row = 1, padx=20, column = 0)
    sps_label = tk.Label(sim_box, text = "Parallel Spring", width=27, bg="white", font = ("arial black", 12)).grid(row = 1, column = 1)
    ses_label = tk.Label(sim_box, text = "Series Spring", width=27, bg="white", font = ("arial black", 12)).grid(row = 1, padx=20, column = 2)

    sis_button = tk.Button(sim_box, image = sis_pic, command = single_win).grid(row = 2, padx=20, column = 0)
    sps_button = tk.Button(sim_box, image = sps_pic, command = series_win).grid(row = 2, column = 1)
    ses_button = tk.Button(sim_box, image = ses_pic, command = parallel_win).grid(row = 2, padx=20, column = 2)
    
    # Add close button functionality
    sim_box.protocol("WM_DELETE_WINDOW", sim_box.destroy) 
    ok_btn = tk.Button(sim_box, width = 10, font=("Arial Black", 10), text="OK", command=sim_box.destroy).grid(row=3, columnspan=3, sticky="E", padx=20, pady=10)
    sim_box.mainloop()

########################################################################
##help button msgbox functions
def help_click():
    help_box = tk.Toplevel(mw, bg="#ADD8E6")
    help_box.title("Help Button")
    
    help_pic = Image.open("Help button pic.png")
    foto = ImageTk.PhotoImage(help_pic)
    
    help_lab = tk.Label(help_box, image = foto)
    help_lab.image = foto
    help_lab.grid(row= 0, column= 0, padx=20, pady=10)
        
    # Add close button functionality
    help_box.protocol("WM_DELETE_WINDOW", help_box.destroy) 
    ok_btn = tk.Button(help_box, width = 10, font=("Arial Black", 10), text="OK", command=help_box.destroy).grid(sticky="E", padx=20, pady=10)

    help_box.mainloop()

####################################################################################
##quiz button msgbox functions
def quiz_pg():
    mw.destroy()
    import hl_quiz

def reset_but():
    f_scale.set(1)
    f_scale.config()
    
    x_scale.set(0.01)
    x_scale.config()
    
    k_scale.set(1)
    k_scale.config
################################################################
##functions to switch scales when button is clicked
def f_func():
    ##change the colour button when selected and remove any other colour for the unselected one
    k_butt.config(background = '#87CEFF')
    f_butt.config(background = '#B0E2FF')
    x_butt.config(background = '#87CEFF')
    ##erasing any previous widgets on screen
    f_scale.set(1)
    f_scale.config()
    
    x_scale.set(0.01)
    x_scale.config()
    
    k_scale.set(1)
    k_scale.config()

    f_ans.config(text="F = 0.01 N")
    k_ans.config(text="k = 100 N/m")
    x_ans.config(text="x = 1.00 m") 

    f_scale.grid_forget()
    f_lab.grid_forget()
    read_f.grid_forget()
    x_ans.grid_forget()
    k_ans.grid_forget()

    ##inserting widgets besides for F variable
    x_scale.grid(row = 3, column = 1, columnspan = 3)
    x_lab.grid(row = 3, column = 0)
    read_x.grid(row = 3, column = 4)
    
    k_scale.grid(row = 4, column = 1, columnspan = 3)
    k_lab.grid(row = 4, column = 0)
    read_k.grid(row = 4, column = 4)

    f_ans.grid(row = 5, rowspan = 2, columnspan = 5)

def x_func():
    ##change the colour button when selected and remove any other colour for the unselected one
    k_butt.config(background = '#87CEFF')
    f_butt.config(background = '#87CEFF')
    x_butt.config(background = '#B0E2FF')
    ##erasing any previous widgets on screen
    f_scale.set(1)
    f_scale.config()
    
    x_scale.set(0.01)
    x_scale.config()
    
    k_scale.set(1)
    k_scale.config()

    f_ans.config(text="F = 0.01 N")
    k_ans.config(text="k = 100 N/m")
    x_ans.config(text="x = 1.00 m") 

    x_scale.grid_forget()
    x_lab.grid_forget()
    read_x.grid_forget()
    f_ans.grid_forget()
    k_ans.grid_forget()

    ##inserting widgets besides for x variable    
    f_scale.grid(row = 3, column = 1, columnspan = 3)
    f_lab.grid(row = 3, column = 0)
    read_f.grid(row = 3, column = 4)
    
    k_scale.grid(row = 4, column = 1, columnspan = 3)
    k_lab.grid(row = 4, column = 0)
    read_k.grid(row = 4, column = 4)

    x_ans.grid(row = 5, rowspan = 2, columnspan = 5)
    
def k_func():
    ##change the colour button when selected and remove any other colour for the unselected one
    k_butt.config(background = '#B0E2FF')
    f_butt.config(background = '#87CEFF')
    x_butt.config(background = '#87CEFF')

    ##erasing any previous widgets on screen
    f_scale.set(1)
    f_scale.config()
    
    x_scale.set(0.01)
    x_scale.config()
    
    k_scale.set(1)
    k_scale.config()

    f_ans.config(text="F = 0.01 N")
    k_ans.config(text="k = 100 N/m")
    x_ans.config(text="x = 1.00 m") 

    k_scale.grid_forget()
    k_lab.grid_forget()
    read_k.grid_forget()
    f_ans.grid_forget()
    x_ans.grid_forget()

    ##inserting widgets besides for k variable
    f_scale.grid(row = 3, column = 1, columnspan = 3)
    f_lab.grid(row = 3, column = 0)
    read_f.grid(row = 3, column = 4)
    
    x_scale.grid(row = 4, column = 1, columnspan = 3)
    x_lab.grid(row = 4, column = 0)
    read_x.grid(row = 4, column = 4)

    k_ans.grid(row = 5, rowspan = 2, columnspan = 5)

######################################################################
##functions to calculate force, extension and spring constant using Hooke's Law (single spring)
def calc_fkx(): 
    f = float(f_scale.get())
    x = float(x_scale.get())
    k = float(k_scale.get())

    if f == 1:
        calc_f = k * x
        fin_ans_f = str(round(calc_f,2))
        f_ans.config(text=f"F = {fin_ans_f} N")

    if k == 1:
        calc_k = f / x
        fin_ans_k = str(abs(round(calc_k, 2)))
        k_ans.config(text = f"k = {fin_ans_k} N/m")

    if x == 0.01:
        calc_x = f / k
        fin_ans_x = str(round(calc_x, 2))
        x_ans.config(text = f"x = {fin_ans_x} m")

######################################################################

##functions to update the graph based on scale
def update_graph():
    ######################################################################
    ##Get the values of force and extension scales
    global force_1, extension_1, force_2, extension_2
    force_1 = float(f_scale.get())
    extension_1 = float(x_scale.get())
    k_1 = float(k_scale.get())

    #Get the value of f_ans label
    value_f = f_ans.cget("text")
    start_index_f = value_f.find("=") + 1
    end_index_f = value_f.find("N")
    extracted_value_f = value_f[start_index_f:end_index_f].strip()
    force_2 = float(extracted_value_f)
    
    #Get the value of x_ans label
    value_x = x_ans.cget("text") 
    start_index_x = value_x.find("=") + 1
    end_index_x = value_x.find("N")
    extracted_value_x = value_x[start_index_x:end_index_x].strip() 
    extension_2 = float(extracted_value_x) 
    
    ######################################################################
    #Graph animation part
    if force_2 != 0.01:
        force = k_1 * extension_1
        if abs(force) > 100:
            force = 100 if force > 0 else -100
            
        x = 250 + extension_1 * 2 * 100
        y = 250 - force_2 * 1.5
        
        graph.delete("dot")
        graph.create_oval(x-5, y-5, x+5, y+5, fill="red", tags="dot")
        
        graph.delete("line")
        graph.create_line(250, 250, x, y, width=2, fill="red", tags="line")
        
        # Calculate area under the line
        EPE = abs(round(((force * extension_1) * 0.5), 4))
        area_label.config(text=f"Elastic Potential Energy = {EPE} J")

    elif extension_2 != 1.00: 
        x = 250 + (force_1/k_1) * 2
        y = 250 - force_1 * 1.5
        
        graph.delete("dot")
        graph.create_oval(x-5, y-5, x+5, y+5, fill="red", tags="dot")
        
        graph.delete("line")
        graph.create_line(250, 250, x, y, width=2, fill="red", tags="line")
        
        # Calculate area under the line
        EPE = abs(round(((force_1**2) / k_1 * 0.5), 4))
        area_label.config(text=f"Elastic Potential Energy = {EPE} J")

    else:
        x = 250 + extension_1 * 100 * 2
        y = 250 - force_1 * 1.5
        
        graph.delete("dot")
        graph.create_oval(x-5, y-5, x+5, y+5, fill="red", tags="dot")
        graph.delete("line")
        graph.create_line(250, 250, x, y, width=2, fill="red", tags="line")
    
        # Calculate area under the line
        EPE = abs(round(((force_1 * extension_1) * 0.5), 4))
        area_label.config(text=f"Elastic Potential Energy = {EPE} J")
    
######################################################################
##functions to connect the scale to the final answer output, graph animation and spring animation
def scale_func(value):
    #Change the side bar figure according to the scale 
    selection_k = str(k_scale.get()) + " N/m"
    read_k.config(text = selection_k)
    selection_x = str(x_scale.get()) + " m"
    read_x.config(text = selection_x)
    selection_F = str(f_scale.get()) + " N"
    read_f.config(text = selection_F)

    ##Graph aniamtion part
    update_graph()

    ##Calculate force, extension and spring constant final output part 
    calc_fkx() 

    ##Spring animation part 
    resize_image(force_1, extension_1, force_2, extension_2)

#########################################################################
##inserting buttons on top panel
intro = tk.Button(mw, text = "Introduction", width = 14, relief = tk.RIDGE, font = ('helvetica', 14), bg = "white", activebackground = 'dark grey', command = introduction_click)
intro.grid(row = 0, column = 0)

theo = tk.Button(mw, text = "Theory", width = 14, relief = tk.RIDGE, font = ('helvetica', 14), bg = "white", activebackground = 'dark grey', command = theory_click)
theo.grid(row = 0, column = 1)

simul_mode = tk.Button(mw, text = "Simulation Mode", width = 14, relief = tk.RIDGE, font = ('helvetica', 14), bg = "white", activebackground = 'dark grey', command = simulation_click)
simul_mode.grid(row = 0, column = 2)

quiz = tk.Button(mw, text = "Quiz", width = 14, relief = tk.RIDGE, font = ('helvetica', 14), bg = "white", activebackground = 'dark grey', command = quiz_pg)
quiz.grid(row = 0, column = 3)

help = tk.Button(mw, text = "HELP", width = 14, relief = tk.RIDGE, font = ('Arial Black', 11), fg = "red", bg = "white", activebackground = 'dark grey', command = help_click)
help.grid(row = 0, column = 4)

################################################################################
##inserting reset buttons 
reset_but = tk.Button(mw, text = "RESET", width = 17, relief = tk.RIDGE, bg = "white", activebackground = 'dark grey', font = ('Arial Black', 11), command = reset_but)
reset_but.grid(row = 2, column = 3, columnspan=2)

################################################################################
##Inserting buttons for variable choice (F, x, or k)
f_butt = tk.Button(mw, text = "F (N)", width = 14, relief = tk.RIDGE, background = '#B0E2FF', font = ('helvetica', 14), command = f_func)
f_butt.grid(row = 2, column = 0)

x_butt = tk.Button(mw, text = "x (m)", width = 14, relief = tk.RIDGE, background = '#87CEFF', font = ('helvetica', 14), command = x_func)
x_butt.grid(row = 2, column = 1)

k_butt = tk.Button(mw, text = "k (N/m)", width = 14, relief = tk.RIDGE, background = '#87CEFF', font = ('helvetica', 14), command = k_func)
k_butt.grid(row = 2, column = 2)

####################################################################################
##Creating variables for scale-side label
read_f = tk.Label(mw, borderwidth = 1, relief = "solid", width = 10, text = "1.00 N", font = ("helvetica", 14), bg = "#FFE4C4")
read_x = tk.Label(mw, borderwidth = 1, relief = "solid", width = 10, text = "1.00 m", font = ("helvetica", 14), bg = "#FFE4C4")
read_k = tk.Label(mw, borderwidth = 1, relief = "solid", width = 10, text = "1.00 N/m", font = ("helvetica", 14), bg = "#FFE4C4")

################################################################################
##Creating scale labels
f_lab = tk.Label(mw, borderwidth = 1, relief = "solid", width = 10, text = "F (N)", bg = "#FFE4C4", font = ("helvetica", 14))

x_lab = tk.Label(mw, borderwidth = 1, relief = "solid", width = 10, text = "x (m)", bg = "#FFE4C4", font = ("helvetica", 14))

k_lab = tk.Label(mw, borderwidth = 1, relief = "solid", width = 10, text = "k (N/m)", bg = "#FFE4C4", font = ("helvetica", 14))

###############################################################################
##Creating final answer labels
f_ans = tk.Label(mw, borderwidth = 1, relief = "solid", width = 14, text = "F = 0.01 N", bg = "#FFE4C4", font = ("helvetica", 14))

x_ans = tk.Label(mw, borderwidth = 1, relief = "solid", width = 14, text = "x = 1.00 m", bg = "#FFE4C4", font = ("helvetica", 14))

k_ans = tk.Label(mw, borderwidth = 1, relief = "solid", width = 14, text = "k = 100 N/m", bg = "#FFE4C4", font = ("helvetica", 14))

######################################################################
##Creating F, x and k scale
f_scale = tk.Scale(mw, from_ = -100, to = 100,
                   orient = tk.HORIZONTAL,
                   length = 400,
                   bg = "light green",
                   bd = 5,
                   resolution = 1,
                   command = scale_func)
f_scale.set(1)

x_scale = tk.Scale(mw, from_ = -1.00, to = 1.00,
                   orient = tk.HORIZONTAL,
                   length = 400,
                   bg = "light green",
                   bd = 5,
                   resolution = 0.01,
                   command = scale_func)
x_scale.set(0.01)

k_scale = tk.Scale(mw, from_ = 1, to = 100,
                   orient = tk.HORIZONTAL,
                   length = 400,
                   bg = "light green",
                   bd = 5,
                   resolution = 1,
                   command = scale_func)
k_scale.set(1)

############################################################################
##Initialise the F scale
x_scale.grid(row = 3, column = 1, columnspan = 3)
x_lab.grid(row = 3, column = 0)
read_x.grid(row = 3, column = 4)
    
k_scale.grid(row = 4, column = 1, columnspan = 3)
k_lab.grid(row = 4, column = 0)
read_k.grid(row = 4, column = 4)

f_ans.grid(row = 5, rowspan = 2, columnspan = 5)

###########################################################################
##Create graph aniamtion
graph.create_line(50, 250, 450, 250, width=2)
graph.create_line(250, 50, 250, 450, width=2)

#drawing scale for x-axes
for i in range(-4, 5): ###(-100, -101, -20)
    y = i * 50 + 250
    graph.create_line(y, 250, y, 245, width=2)
    graph.create_text(y, 260, text=str((i * 25)/100), anchor= tk.N)

#drawing scale for y-axes
for i in range(100, -101, -20): ## (-4,5)
    x = 250 - i * 1.5
    graph.create_line(250, x, 255, x, width=2)
    graph.create_text(240, x, text=str((i)), anchor= tk.E)
    

#writing axes labels
graph.create_text(250, 15, text="Force (N)", font=("Helvetica", 18), anchor= tk.N)
graph.create_text(15, 300, text="Extension (m)", font=("Helvetica", 18), angle=90, anchor= tk.W)



#Label to display area under the line
area_label = tk.Label(mw, text="Elastic Potential Energy = 0.0 Nm", font=("Helvetica", 14), width=45, bg="white")
area_label.grid(row = 6, column = 5)

##########################################################################################

mw.mainloop()