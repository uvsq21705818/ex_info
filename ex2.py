import tkinter as tk
import random as rd

HEIGHT = 500
WIDTH = HEIGHT

nb_clic = 0
x0 = 0
x1 = 0
y0 = 0
y1 = 0
paused = False

def pause():
    global paused
    bouton_pause.config(text="RESTART", command=restart)
    paused = True

def restart():
    global paused
    bouton_pause.config(text="PAUSE", command=pause)
    paused = False

def clic_ligne(event):
    global nb_clic
    global x0, x1, y0, y1

    if paused == False:
        if nb_clic == 0:
            x0 = event.x
            y0 = event.y
            nb_clic += 1
        elif nb_clic == 1:
            x1 = event.x
            y1 = event.y
            canevas.create_line(x0, y0, x1, y1, fill="blue")
            nb_clic += 1
        elif nb_clic == 2:
            x0 = event.x
            y0 = event.y
            nb_clic += 1
        elif nb_clic == 3:
            x1 = event.x
            y1 = event.y
            canevas.create_line(x0, y0, x1, y1, fill="red")
            nb_clic += 1
        elif nb_clic == 4:
            canevas.delete("all")
            nb_clic = 0



root = tk.Tk()

canevas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="white")
bouton_pause = tk.Button(root, text="PAUSE", command=pause)


canevas.grid(row=0, column=0)
bouton_pause.grid(row=1, column=0)
canevas.bind('<Button-1>', clic_ligne)

root.mainloop()