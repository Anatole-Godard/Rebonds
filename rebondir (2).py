from tkinter import *
import random
import time

class Balle: #les classe sont des familles d'objet qui sont définie par des carractéristiques . 
    def __init__(self, canvas, raquette, couleur):# 'def' est une fonction.
        #Les fonctions peuvent être réutiliser, je juste par un nom que l'on lui attribut, pour avoir moins de ligne dans le programme. 
        self.canvas = canvas
        self.raquette = raquette
        self.id = canvas.create_oval(10, 10, 25, 25, fill=couleur)
        self.canvas.move(self.id, 245, 100)
        departs = [-3, -2, -1, 1, 2, 3]
        random.shuffle(departs)
        self.x = departs[0]
        self.y = -3
        self.hauteur_canevas = self.canvas.winfo_height()
        self.largeur_canevas = self.canvas.winfo_width()
        self.touche_bas = False
    
    def heurter_raquette(self, pos):
        pos_raquette = self.canvas.coords(self.raquette.id)
        if pos[2] >= pos_raquette[0] and pos[0] <= pos_raquette[2]:
            if pos[3] >= pos_raquette[1] and pos[3] <= pos_raquette[3]:
                return True
            return False
        
    def dessiner(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.hauteur_canevas:
            self.touche_bas = True
        if self.heurter_raquette(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.largeur_canevas:
            self.x = -3

class Raquette:
    def __init__(self, canvas, couleur):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=couleur)
        self.canvas.move(self.id, 260, 300)
        self.x = 0
        self.largeur_canevas = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.vers_gauche)
        self.canvas.bind_all('<KeyPress-Right>', self.vers_droite)
        self.canvas.bind_all('<KeyPress-Down>', self.arreter_raquette)
        
        
    def vers_gauche(self, evt):
        self.x = -3

    def vers_droite(self, evt):
        self.x = 3
        
    def arreter_raquette(self, evt):
        self.x = 0
        self.y = 0
        
        
    def dessiner(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.largeur_canevas:
            self.x = 0
            
tk = Tk()
tk.title("Jeu")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd = 8, highlightthickness=0, bg='grey', relief = 'ridge')
canvas.pack()
tk.update()

bouton_sortir = Button(tk, text="Sortir", command = tk.destroy)
bouton_sortir.pack()

raquette = Raquette(canvas, 'red')
balle = Balle(canvas, raquette, 'black')

while 1:
    if balle.touche_bas == False:
        balle.dessiner()
        raquette.dessiner()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
