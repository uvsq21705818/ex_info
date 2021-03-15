import tkinter as tk

HEIGHT = 500
WIDTH = 500

coord_carre = []
paused = False

def pause():
    global paused
    bouton_pause.config(text="RESTART", command=restart)
    paused = True

def restart():
    global paused
    bouton_pause.config(text="PAUSE", command=pause)
    paused = False

def clic(event):
    x, y = event.x, event.y
    if paused == False:
        if coord_carre[0] < x < coord_carre[2] and coord_carre[1] < y < coord_carre[3]:
            clic_int(x,y)
        else:
            clic_ext(x,y)

def clic_int(x,y):
    global coord_carre

    if coord_carre[2] - coord_carre[0] >= 20:
        coord_carre[0] += 5
        coord_carre[1] += 5
        coord_carre[2] -= 5
        coord_carre[3] -= 5
        canvas.delete("all")
        canvas.create_rectangle(coord_carre[0], coord_carre[1], coord_carre[2], coord_carre[3], fill="red")

def clic_ext(x,y):
    global coord_carre

    if coord_carre[2] - coord_carre[0] <= 100:
        coord_carre[0] -= 5
        coord_carre[1] -= 5
        coord_carre[2] += 5
        coord_carre[3] += 5
        canvas.delete("all")
        canvas.create_rectangle(coord_carre[0], coord_carre[1], coord_carre[2], coord_carre[3], fill="red")

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="white")
bouton_pause = tk.Button(root, text="PAUSE", command=pause)

canvas.create_rectangle((WIDTH/2) - 25, (HEIGHT/2) - 25, (WIDTH/2) + 25, (HEIGHT/2) + 25, fill="red")
coord_carre = [(WIDTH/2) - 25, (HEIGHT/2) - 25, (WIDTH/2) + 25, (HEIGHT/2) + 25]

canvas.grid(row=0, column=0)
bouton_pause.grid(row=1, column=0)
canvas.bind("<Button-1>", clic)

root.mainloop()