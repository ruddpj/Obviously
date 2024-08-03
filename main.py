from tkinter import *

root = Tk(className="Obviously")
canvas = Canvas(width=800, height=1000)
canvas.pack()

c_box = "blue"
c_text = "white"
f_size = "Arial 18"
b_size = "Arial 32"

red_pts = 0
blue_pts = 0

file_1 = open("obv_topics.txt", "r", encoding="utf8")
x, y = 100, 100
count = 1
for i in range(3):
    for j in range(3):
        o = file_1.readline()
        canvas.create_rectangle(x, y, x + 200, y + 200, fill=c_box, outline="black", tags=f"b{count}")
        canvas.create_text(x + 100, y + 116, text=f"{count}:\n{o}", font=f_size, fill="white")
        x += 200
        count += 1
    x = 100
    y += 200
file_1.close()
canvas.create_text(200, 900, text=f"TEAM RED: {red_pts}", font=f_size, fill="black", tags=f"red")
canvas.create_text(600, 900, text=f"TEAM BLU: {red_pts}", font=f_size, fill="black", tags=f"blu")


def points_adder(side, pts):
    global red_pts, blue_pts
    if side == 0:
        red_pts += int(pts)
        canvas.itemconfig("red", text=f"TEAM RED: {str(red_pts)}")
    else:
        blue_pts += int(pts)
        canvas.itemconfig("blu", text=f"TEAM BLU: {str(blue_pts)}")


def q_cords(get, side, new, arr):
    a = get.x
    b = get.y
    if 750 <= b < 800:
        if 300 <= a <= 350:
            new.delete("all")
            Misc.lift(canvas)
        elif 400 <= a <= 450:
            new.create_text(400, 400, text="0 POINTS", font="Arial 72", fill="black", tags="temp")
            new.after(2000, lambda: new.delete("temp"))
        elif 350 < a < 400:
            new.create_text(400, 400, text="100 POINTS", font="Arial 72", fill="black", tags="temp")
            new.after(2000, lambda: new.delete("temp"))
            points_adder(side, 100)
    elif 200 <= a <= 600:
        if 100 < b < 160:
            points_adder(side, arr[0])
            new.itemconfig(f"a{0}", fill="blue")
        elif 160 < b < 220:
            points_adder(side, arr[1])
            new.itemconfig(f"a{1}", fill="blue")
        elif 220 < b < 280:
            points_adder(side, arr[2])
            new.itemconfig(f"a{2}", fill="blue")
        elif 280 < b < 340:
            points_adder(side, arr[3])
            new.itemconfig(f"a{3}", fill="blue")
        elif 340 < b < 400:
            points_adder(side, arr[4])
            new.itemconfig(f"a{4}", fill="blue")
        elif 400 < b < 460:
            points_adder(side, arr[5])
            new.itemconfig(f"a{5}", fill="blue")
        elif 460 < b < 520:
            points_adder(side, arr[6])
            new.itemconfig(f"a{6}", fill="blue")
        elif 520 < b < 580:
            points_adder(side, arr[7])
            new.itemconfig(f"a{7}", fill="blue")
        elif 580 < b < 640:
            points_adder(side, arr[8])
            new.itemconfig(f"a{8}", fill="blue")


def open_q_canvas(tp):
    cat = []
    pts_cat = []
    file_2 = open(f"answers/{tp}.txt", "r", encoding="utf8")
    new_c = Canvas(root, width=800, height=800)
    new_c.place(x=0, y=0)

    new_c.bind("<Button-1>", lambda event: q_cords(event, 0, new_c, pts_cat))
    new_c.bind("<Button-3>", lambda event: q_cords(event, 1, new_c, pts_cat))

    f, g = 200, 100
    new_c.create_text(400, 70, text=f"{file_2.readline()}", font="Arial 24", fill="black")

    for cout in range(9):
        text_a = file_2.readline().strip()
        text_b = file_2.readline().strip()
        cat.append(text_a)
        pts_cat.append(text_b)
        new_c.create_rectangle(f, g, f + 400, g + 60, fill="white", outline="black", tags=f"a{cout}")
        new_c.create_text(f + 200, g + 30, text=f"{text_a} {text_b}", font=f_size, fill="white")
        g += 60
    new_c.create_rectangle(300, 750, 350, 800, fill="white", outline="black")
    new_c.create_text(325, 775, text="X", font=b_size, fill="black")
    new_c.create_rectangle(400, 750, 450, 800, fill="white", outline="black")
    new_c.create_text(425, 775, text="0", font=b_size, fill="black")
    new_c.create_rectangle(350, 750, 400, 800, fill="white", outline="black")
    new_c.create_text(375, 775, text="100", font="Arial 18", fill="black")

    file_2.close()


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
        canvas.itemconfig(f"b{topic}", fill="gray")
        open_q_canvas(topic)


canvas.bind("<Button-1>", cords)

root.mainloop()
