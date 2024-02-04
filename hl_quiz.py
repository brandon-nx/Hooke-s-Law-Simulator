import tkinter as tk
import random

root = tk.Tk()
root.title("Test Yourself")
root.config(bg = '#4682B4')

wrongquestionlist=[]
questions = [
    {
        "question": "Question 1: During inelastic collision of two bodies, which of the following quantities is conserved?",
        "options": ["Total Kinetic Energy", "Total Mechanical Energy", "Total Linear Momentum", "Speed of the Two Bodies"],
        "answer": "Total Linear Momentum"
    },
    {
        "question": "Question 2: A ball of 2kg moving at 5m/s strikes another mass of 3kg at rest.\n If they move together after collision, what is their new common velocity? ",
        "options": ["1m/s", "2m/s", "3m/s", "4m/s"],
        "answer": "2m/s"
    },
    {
        "question": "Question 3: A bullet of mass 20 g is fired from a gun of mass 2.5 kg.\n The bullet leaves the gun with average velocity of 500 m s–1.\n Find the initial velocity of recoil of the gun",
        "options": ["-4m/s", "4m/s", "10m/s", "-10m/s"],
        "answer": "-4m/s"
    },
    {
        "question": "Question 4: For what value of e(coefficient of restitution) is a collision perfectly elastic?",
        "options": ["1", "2", "0.5", "0"],
        "answer": "1"
    },
    {
        "question": "Question 5: A car of mass 1 ton is moving with a velocity of 25 m/s towards left.\n A truck of mass 5 ton is moving towards left with a velocity of 3 m/s.\n If the collision is perfectly elastic, what is the final velocity of the truck in m/s?",
        "options": ["11", "25", "3", "10"],
        "answer": "3"
    }
]


border_color = tk.Frame(root, background= 'white')
border_color.grid(row = 2, columnspan = 4, padx = 10, pady = 10)
question_label = tk.Label(border_color, text="", font = ("Arial Bold", 15), bg = '#5F9EA0', fg= 'white')
question_label.grid(row = 2, columnspan = 4, padx = 1, pady = 1)

option_buttons = []
x = 0
for i in range(4):
    button = tk.Button(root, text="", command=lambda i=i: select_option(i), font = ("Arial", 16),fg = "grey33", activebackground= '#CCCCFF', bg = 'light green', padx= 2)
    option_buttons.append(button)
    button.grid(row = 3, column = x, padx = 10)
    x += 1

def main_pg():
    root.destroy()
    import hl_single_spring

feedback_label = tk.Label(root, text="")
feedback_label.grid(row = 4, padx = 10, pady = 10)

def select_option(option_index):
    global current_question_index,wrongquestionlist
    questions[current_question_index]["selected_option"] = option_index
    selected_option = questions[current_question_index]["options"][option_index]
    correct_answer = questions[current_question_index]["answer"]
    if selected_option == correct_answer:
        feedback_label.config(text="Correct!")
    else:
        feedback_label.config(text="Incorrect!")
        wrongquestionlist.append(current_question_index)
    current_question_index += 1
    if current_question_index < len(questions):
        display_question(current_question_index)
    else:
        finish_test()

def display_question(question_index):
    question = questions[question_index]
    random.shuffle(question["options"])
    question_label.config(text=question["question"])
    for i in range(4):
        option_buttons[i].config(text=question["options"][i])

    feedback_label.config(text="")

def finish_test():
    global wrongquestionlist
    question_label.config(text="")
    for button in option_buttons:
        button.destroy()
    correct_answers = 0
    text1="wrong question and corresponding answer"
    for x in wrongquestionlist:
        text1=text1+"\n"+questions[x]["question"]+"\nanswer:"+questions[x]["answer"]
    for question in questions:
        if question["answer"] == question["options"][question["selected_option"]]:
            correct_answers += 1
    feedback_label.config(text="Test completed! You scored {}/{}\n{}.".format(correct_answers, len(questions),text1), font = ("Arial", 15), bg = '#CC99FF')

current_question_index = 0
display_question(current_question_index)

quit_button = tk.Button(root, text="Quit", font=("Arial black", 10), bg='#9A32CD', command=main_pg)
quit_button.grid(row = 0, column = 3, sticky="E", padx = 10, pady = 10)

root.mainloop()
# To craete a list
