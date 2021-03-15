import tkinter as tk

HEIGHT = 500
WIDTH = 500

nb_croix = 0
nb_carre = 0
nb_cercle = 0

def clic_milieu(x,y):
    global nb_carre, nb_croix
    if nb_carre < 3:
        canvas.create_rectangle(x - 25, y - 25, x + 25, y + 25, fill="green")
        nb_carre += 1
def clic_droite(x,y):
    global nb_cercle
    if nb_cercle < 3:
        canvas.create_oval(x - 25, y - 25, x + 25, y + 25, fill="red")
        nb_cercle += 1

def clic_gauche(x,y):
    global nb_carre, nb_croix
    if nb_croix < 2:
        canvas.create_rectangle(x - 25, y - 25, x + 25, y + 25, fill="white")
        canvas.create_line(x - 25, y - 25, x + 25, y + 25, fill="blue")
        canvas.create_line(x + 25, y - 25, x - 25, y + 25, fill="blue")
        nb_croix += 1
        nb_carre += 1

def clic(event):
    x, y = event.x, event.y
    if x < WIDTH / 3:
        clic_gauche(x,y)
    elif WIDTH / 3 < x < (2 * WIDTH) / 3:
        clic_milieu(x,y)
    elif x > (2 * WIDTH) / 3:
        clic_droite(x,y)

def restart():
    global nb_croix, nb_carre, nb_cercle
    canvas.delete("all")
    canvas.create_line(WIDTH / 3, 0, WIDTH / 3, HEIGHT, fill="white")
    canvas.create_line((2 * WIDTH) / 3, 0, (2 * WIDTH) / 3, HEIGHT, fill="white")
    nb_carre = 0
    nb_croix = 0
    nb_cercle = 0

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="black")
bouton_restart = tk.Button(root, text="REDEMARRER", command=restart)

canvas.create_line(WIDTH / 3, 0, WIDTH / 3, HEIGHT, fill="white")
canvas.create_line((2 * WIDTH) / 3, 0, (2 * WIDTH) / 3, HEIGHT, fill="white")

canvas.grid(row=0, column=0)
bouton_restart.grid(row=1, column=0)
canvas.bind("<Button-1>", clic)

root.mainloop()