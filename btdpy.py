from tkinter import Tk,simpledialog, messagebox ,Button,Label
import math

def positive(event):
    firstnum = simpledialog.askfloat('number','Type the first number: ')
    secnum = simpledialog.askfloat('number','Type the second number: ')
    result = (firstnum + secnum)
    messagebox.showinfo('Answer','positive result is ' + str(result))
    

def negative(event):
    firstnum = simpledialog.askfloat('number','Type the first number: ')
    secnum = simpledialog.askfloat('number','Type the second number: ')
    result = (firstnum - secnum)
    messagebox.showinfo('Answer','negative result is ' + str(result))
    
def multiply(event):
    firstnum = simpledialog.askfloat('number','Type the first number: ')
    secnum = simpledialog.askfloat('number','Type the second number: ')
    result = (firstnum * secnum)
    messagebox.showinfo('Answer','multiply result is ' + str(result))

def divide(event):
     firstnum = simpledialog.askfloat('number','Type the first number: ')
     secnum = simpledialog.askfloat('number','Type the second number: ')
     result = (firstnum / secnum)
     messagebox.showinfo('Answer','divide result is ' + str(result))

def modulus(event):
     firstnum = simpledialog.askfloat('number','Type the first number: ')
     secnum = simpledialog.askfloat('number','Type the second number: ')
     result = (firstnum % secnum)
     messagebox.showinfo('Answer','modulus result is ' + str(result))
     
def	Exponentiation(event):
     firstnum = simpledialog.askfloat('number','Type the first number: ')
     secnum = simpledialog.askfloat('number','Type the second number: ')
     result = (firstnum ** secnum)
     messagebox.showinfo('Answer','Exponentiation result is ' + str(result))
	
def	percentage(event):
     firstnum = simpledialog.askfloat('number','Type the first number(maximum): ')
     secnum = simpledialog.askfloat('number','Type the second number: ')
     result = (secnum/firstnum)*100
     messagebox.showinfo('Answer','percentage result is ' + str(result))
     
def pythagorus_short(event):
     side1 =simpledialog.askfloat('number','Type the first side: ')
     side2 =simpledialog.askfloat('number','Type the second side: ')
     result = math.sqrt((side1**2)-(side2**2))
     messagebox.showinfo('Answer','pythagorus short side result is ' + str(result))    
     
def pythagorus_long(event):
     side1 =simpledialog.askfloat('number','Type the first side: ')
     side2 =simpledialog.askfloat('number','Type the second side: ')
     result = math.sqrt((side1**2)+(side2**2))
     messagebox.showinfo('Answer','pythagorus long result is ' + str(result))  

def square_space(event):
     side1 =simpledialog.askfloat('number','Type the first side: ')
     side2 =simpledialog.askfloat('number','Type the second side: ')
     result = (side1*side2)
     messagebox.showinfo('Answer','square space is ' + str(result)) 
     
def triangle_space(event):
     b =simpledialog.askfloat('number','Type the base: ')
     t =simpledialog.askfloat('number','Type tall: ')
     result = (0.5*b*t)
     messagebox.showinfo('Answer','triangle space is ' + str(result)) 
     
def circle_space(event):
    R =simpledialog.askfloat('number','Type the radius: ')  
    result = math.pi*R*R
    messagebox.showinfo('Answer','circle space is ' + str(result)) 
    
def circle_perimeter(event):
    R =simpledialog.askfloat('number','Type the radius: ')  
    result = 2*math.pi*R
    messagebox.showinfo('Answer','circle perimete is ' + str(result)) 
    
def pentagon_area(event):
    side =simpledialog.askfloat('number','Type the side: ')
    result = (side ** 2 * math.sqrt(5 * (5 + 2 * math.sqrt(5)))) / 4
    messagebox.showinfo('Answer','pentagon area is ' + str(result))
    
def rhombus_area(event):
    d1 =simpledialog.askfloat('number','Type the first diagonal: ')
    d2 =simpledialog.askfloat('number','Type the second diagonal: ')
    result = (1/2)*d1*d2
    messagebox.showinfo('Answer','rhombus area is ' + str(result))
    
def octagon_area(event):
    d =simpledialog.askfloat('number','Type the diagonal: ')
    result = 2 * (1 + math.sqrt(2)) * d ** 2
    messagebox.showinfo('Answer','octagon area is ' + str(result))
    
def hexagon_area(event):
    s =simpledialog.askfloat('number','Type side: ')
    result = (3 * math.sqrt(3) * s ** 2) / 2
    messagebox.showinfo('Answer','hexagon area is ' + str(result))

def sphere_area(event):
    R =simpledialog.askfloat('number','Type the radius: ') 
    result = 4 * math.pi * R **2
    messagebox.showinfo('Answer','sphere area is ' + str(result))
    
def vol_pyramid(event):
    b =simpledialog.askfloat('number','Type the base: ')
    t =simpledialog.askfloat('number','Type tall: ')
    result = (b * t) /3
    messagebox.showinfo('Answer','volume of pyramid is ' + str(result))
    
MainWindow = Tk()

posbutton = Button(MainWindow,text= "          plus           ")
posbutton.bind('<Button-1>',positive)
posbutton.grid(row=1,column=0)

negbutton = Button(MainWindow,text = "         negative        ")
negbutton.bind('<Button-1>',negative)
negbutton.grid(row=1,column=1)

mulbutton = Button(MainWindow,text = "        multiply        ")
mulbutton.bind('<Button-1>',multiply)
mulbutton.grid(row=1,column=2)

divbutton = Button(MainWindow,text = "            divide           ")
divbutton.bind('<Button-1>',divide)
divbutton.grid(row=1,column=3)

modubutton = Button(MainWindow,text = "      modulus       ")
modubutton.bind('<Button-1>',modulus)
modubutton.grid(row=2,column=0)

exbutton = Button(MainWindow,text = "   Exponentiation   ")
exbutton.bind('<Button-1>',Exponentiation)
exbutton.grid(row=2,column=1)

perbutton = Button(MainWindow,text = "      percentage     ")
perbutton.bind('<Button-1>',percentage)
perbutton.grid(row=2,column=2)

pyshbutton = Button(MainWindow,text ="  pythagorus short  ")
pyshbutton.bind('<Button-1>',pythagorus_short)
pyshbutton.grid(row=2,column=3)

pylbutton = Button(MainWindow,text = "pythagorus long")
pylbutton.bind('<Button-1>',pythagorus_long)
pylbutton.grid(row=3,column=0)

sqbutton = Button(MainWindow,text = "    square  space     ")
sqbutton.bind('<Button-1>',square_space)
sqbutton.grid(row=3,column=1)

tributton = Button(MainWindow,text = "   triangle space    ")
tributton.bind('<Button-1>',triangle_space)
tributton.grid(row=3,column=2)

cirabutton = Button(MainWindow,text = "      circle   space     ")
cirabutton.bind('<Button-1>',circle_space)
cirabutton.grid(row=3,column=3)

cirpbutton = Button(MainWindow,text = " circle perimeter ")
cirpbutton.bind('<Button-1>',circle_perimeter)
cirpbutton.grid(row=4,column=0)

penbutton = Button(MainWindow,text = "    pentagon  area   ")
penbutton.bind('<Button-1>',pentagon_area)
penbutton.grid(row=4,column=1)

rhobutton = Button(MainWindow,text = "   rhombus  area   ")
rhobutton.bind('<Button-1>',rhombus_area)
rhobutton.grid(row=4,column=2)

octbutton = Button(MainWindow,text = "     octagon  area     ")
octbutton.bind('<Button-1>',octagon_area)
octbutton.grid(row=4,column=3)

hexbutton = Button(MainWindow,text = "  hexagon  area  ")
hexbutton.bind('<Button-1>',hexagon_area)
hexbutton.grid(row=5,column=0)

sphbutton = Button(MainWindow,text = "  sphere   area  ")
sphbutton.bind('<Button-1>',sphere_area)
sphbutton.grid(row=5,column=1)

pyvbutton = Button(MainWindow,text = "   volume pyramid   ")
pyvbutton.bind('<Button-1>',vol_pyramid)
pyvbutton.grid(row=5,column=1)

labelthx = Label(MainWindow,text="    CALCULATOR   ")
labelthx.grid(row=5,column=2)
MainWindow.mainloop()