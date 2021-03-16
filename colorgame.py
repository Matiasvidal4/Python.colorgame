from tkinter import *
import random


colores = ["red", "blue", "green", "pink", "yellow", "black", "violet"]
score = 0
tiempo = 30

#configurar la ventana
def contador():
    global tiempo
    if tiempo > 0:
        tiempo -= 1
        timer.config( text ="tiempo: "+ str(tiempo)+ " segundos")
        timer.after(1000, contador)
    else:
        tiempo = 30

def iniciar(event):
    if tiempo == 30:
        contador()
        score = 0
        scoreLabel.config(text = "score: "+ str(score))
    colorShuffle()

def colorShuffle():
    global score
    global timer
    if tiempo > 0:
        if e1.get() == colores[3].lower():
            score += 1
            scoreLabel.config(text = "score: "+ str(score))
        e1.delete(0, END)
        random.shuffle(colores)
        label1.config(text=str(colores[1]), fg=str(colores[3]), font = ("helvetica", 40), bg = "gray")




gui = Tk()
gui.configure(background = "gray")
gui.geometry("500x300")
gui.title("color game")


instructions = Label(gui, text="¡Escribe el color de las palabras y no el texto de estas!", bg="red", fg="white", font=("helvetica", 12, "bold"))
instructions.pack()

instructions2 = Label(gui, text="Presiona enter para empezar", bg="blue", fg="white", font=("helvetica", 12, "bold"))
instructions2.pack()

timer = Label(gui, text="tiempo:"+str(tiempo)+" segundos", bg="green", fg="white", font=("helvetica", 12, "bold"))
timer.pack()

scoreLabel = Label(gui, text="score: "+ str(score), bg="red",fg="white", font=("helvetica", 12, "bold"))
scoreLabel.pack()

label1 = Label(gui)
label1.pack()

tusolabel = Label(gui, text="tuso", bg="gray", fg="white")
tusolabel.place(x = 0, y = 280)

gui.bind("<Return>", iniciar)

e1 = Entry(gui, relief= GROOVE, font = "helvetica")
e1.place(x = 150, y = 200, width=200, height=50)


gui.mainloop()



