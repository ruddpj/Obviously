from tkinter import *

root = Tk(className="Obviously")
canvas = Canvas(width=800, height=800)
canvas.pack()

c_box = "blue"
c_text = "white"
f_size = "Arial 18"

file_1 = open("obv_topics.txt", "r", encoding="utf8")
x, y = 100, 100
count = 1
for i in range(3):
    for j in range(3):
        o = file_1.readline()
        canvas.create_rectangle(x, y, x+200, y+200, fill=c_box, outline="black", tags=f"{count}")
        canvas.create_text(x+100, y+116, text=f"{count}:\n{o}", font=f_size, fill="white")
        x += 200
        count += 1
    x = 100
    y += 200
file_1.close()


def submit(arr, question, new_c):
    ans_var = question.get().strip()
    for itt in range(9):
        if ans_var == arr[itt]:
            new_c.itemconfig(f"a{itt}", fill="blue")
            return
    new_c.create_rectangle(200, 700, 600, 760, fill="blue", outline="black")
    new_c.create_text(400, 730, text=f"0 POINTS", font=f_size, fill="white")


def cords(get):
    a = get.x
    b = get.y
    sig, topic = 0, 0
    if 300 > a > 100:
        topic = 1
        sig += 1
    elif 500 > a > 300:
        topic = 2
        sig += 1
    elif 700 > a > 500:
        topic = 3
        sig += 1
    else:
        sig = 0

    if 300 > b > 100:
        sig += 1
    elif 500 > b > 300:
        topic += 3
        sig += 1
    elif 700 > b > 500:
        topic += 6
        sig += 1
    else:
        sig = 0

    if sig > 1:
        cat = []
        file_2 = open(f"answers/{topic}.txt", "r", encoding="utf8")
        new = Tk(className=f"Topic {topic}")
        new_c = Canvas(new, width=800, height=800)
        new_c.pack()
        f, g = 200, 100
        new_c.create_text(400, 70, text=f"{file_2.readline()}", font="Arial 24", fill="black")

        for cout in range(9):
            text_a = file_2.readline().strip()
            text_b = file_2.readline().strip()
            cat.append(text_a)
            new_c.create_rectangle(f, g, f+400, g+60, fill="white", outline="black", tags=f"a{cout}")
            new_c.create_text(f+200, g+30, text=f"{text_a} {text_b}", font=f_size, fill="white")
            g += 60
            
        file_2.close()
        question = StringVar()
        choose = Entry(root, textvariable=question)
        choose.pack(side=LEFT)
        button = Button(root, text="Submit", command=lambda: submit(cat, question, new_c))
        button.pack(side=RIGHT)
        b_tn = Button(root, text="X", command=lambda: [b_tn.pack_forget(), button.pack_forget(), choose.pack_forget()])
        b_tn.pack()


canvas.bind("<Button-1>", cords)

root.mainloop()
