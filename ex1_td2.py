import tkinter as tk
import random as rd

HEIGHT = 400
WIDTH = 600

balle = []

def start():
    mouvement()
    bouton_start.config(text="ARRETER", command=stop)

def stop():

def creer_balle():
    global balle
    balle.append(canvas.create_oval((WIDTH/2) - 10, (HEIGHT/2) - 10, (WIDTH/2) + 10, (HEIGHT/2) + 10, fill="blue"))
    balle.append(rd.randint(1, 7))
    balle.append(rd.randint(1, 7))


def mouvement():
    canvas.move(balle[0], balle[1], balle[2])
    canvas.after(20, mouvement)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="black")
bouton_start = tk.Button(root, text="DEMARRER", command=start)

balle1 = creer_balle()


canvas.grid(row=0, column=0)
bouton_start.grid(row=1, column=0)

root.mainloop()