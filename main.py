from tkinter import *

root = Tk(className="Obviously")
canvas = Canvas(width=800, height=800)
canvas.pack()

c_box = "blue"
c_text = "white"
f_size = "Arial 32"

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


def opener(q):
    new = Tk(className=f"Topic {q}")
    new_c = Canvas(new, width=800, height=800)
    new_c.pack()
    f, g = 200, 100
    file_2 = open(f"answers/{q}.txt", "r", encoding="utf8")
    cat = []

    new_c.create_text(400, 70, text=f"{file_2.readline()}", font="Arial 24", fill="black")

    for cout in range(9):
        text_a = file_2.readline().strip()
        text_b = file_2.readline().strip()
        cat.append(text_a)
        new_c.create_rectangle(f, g, f+400, g+60, fill="white", outline="black", tags=f"a{cout}")
        new_c.create_text(f+200, g+30, text=f"{text_a} {text_b}", font=f_size, fill="white")
        g += 60

    def submit(arr):
        ans_var = question.get()
        for itt in range(9):
            if ans_var == arr[itt]:
                new_c.itemconfig(f"a{itt}", fill="blue")
                return
        new_c.create_rectangle(200, 700, 600, 760, fill="blue", outline="black")
        new_c.create_text(400, 730, text=f"0 POINTS", font=f_size, fill="white")

    question = StringVar()
    choose = Entry(root, textvariable=question)
    button = Button(root, text="Submit", command=lambda: submit(cat))
    choose.pack(side=LEFT)
    button.pack(side=RIGHT)
    new.mainloop()


def cords(get):
    a = get.x
    b = get.y
    sig, topic = 0, 0
    while sig < 1:
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
            topic += 1
            sig += 1
        elif 700 > b > 500:
            topic += 2
            sig += 1
        else:
            sig = 0
    opener(topic)


canvas.bind("<Button-1>", cords)

root.mainloop()
