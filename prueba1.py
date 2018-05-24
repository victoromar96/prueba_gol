from tkinter import *
import tkinter


tk = Tk()
tk.title("TIRO A LA PORTERIA")
canvas = Canvas(tk, width=820, height=450)
canvas.pack()

my_image = PhotoImage(file= "estadio.gif")
canvas.create_image(0,0, anchor=  NW,image=my_image)

my_image2 = PhotoImage(file= "por.gif")
canvas.create_image(405,220, anchor=  NW,image=my_image2)

my_image3 = PhotoImage(file= "baloon.gif")
canvas.create_image(0,290, anchor=  NW,image=my_image3)

def moveBalon(event):
    canvas.move(3,5,0)

canvas.bind_all('<KeyPress-Right>', moveBalon)
canvas.move(1,5,0)
canvas.move(2,5,0)


#def moveBalon1(event):
#    canvas.move(3,0,5)
#    gol()
#canvas.bind_all('<KeyPress-Down>', moveBalon1)

#
#def moveBalon2(event):
#    canvas.move(3,0,-5)
#    gol()
#canvas.bind_all('<KeyPress-Up>', moveBalon2)

def moveBalon3(event):
    canvas.move(3,-5,0)
    gol()
canvas.bind_all('<KeyPress-Left>', moveBalon3)

meta = Label(text = "gooooooool").place(x=405,y=150)

def gol():
    if my_image3 == my_image2:
        print("golazooo")
    root = tkinter.Tk()
    boton = tkinter.Button(root, text="GOOOOOOOOL!!!!!!!?", command=gol)
    boton.pack()
    root.mainloop()


tk.mainloop()





