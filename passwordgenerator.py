import random
from tkinter import *
from tkinter import messagebox

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', ';', ':', "'", '"', '<', '>', ',', '.', '/', '?']

mainwindow = Tk()
mainwindow.title('PASSWORD GENERATOR')
mainwindow.geometry('900x600')
mainwindow.config(bg='black')

title_label = Label(mainwindow, text='Welcome to PASSWORD GENERATOR !', fg='white', bg='black', font=('Arial', 25,'bold'))
title_label.pack(pady=50,padx=30)

frame=Frame(
    mainwindow,
        padx=10,
        pady=10,
        bg='skyblue',
)
frame.pack(expand=True)

lengthlabel=Label(
    frame,
    text="                     Enter the length of your password             :",
    font=('timesnewroman', 17,'bold'),
    bg='darkblue',
    fg='white')
lengthlabel.grid(row=1,column=1)
lengthtextfield=Entry(frame,font=('timesnewroman', 17,'bold'),
    bg='white',
    fg='darkblue'
                   )
lengthtextfield.grid(row=1,column=2,pady=17)

nalphabetslabel=Label(
    frame,
    text="How many alphabets do you want in your password ?",
    font=('timesnewroman', 17,'bold'),
    bg='darkblue',
    fg='white')
nalphabetslabel.grid(row=2,column=1)
nalphabetstextfield=Entry(frame,font=('timesnewroman', 17,'bold'),
    bg='white',
    fg='darkblue'
                   )
nalphabetstextfield.grid(row=2,column=2,pady=17)

nnumberslabel=Label(
    frame,
    text="How many numbers do you want in your password   ?",
    font=('timesnewroman', 17,'bold'),
    bg='darkblue',
    fg='white')
nnumberslabel.grid(row=3,column=1)
nnumberstextfield=Entry(frame,font=('timesnewroman', 17,'bold'),
    bg='white',
    fg='darkblue'
                   )
nnumberstextfield.grid(row=3,column=2,pady=17)

nsymbolslabel=Label(
    frame,
    text="How many symbols do you want in your password   ?",
    font=('timesnewroman', 17,'bold'),
    bg='darkblue',
    fg='white')
nsymbolslabel.grid(row=4,column=1)
nsymbolstextfield=Entry(frame,font=('timesnewroman', 17,'bold'),
    bg='white',
    fg='darkblue'
                   )
nsymbolstextfield.grid(row=4,column=2,pady=17)


def generatepassword():
    try:
        length=int(lengthtextfield.get())
        nalphabets=int(nalphabetstextfield.get())
        nnumbers=int(nnumberstextfield.get())
        nsymbols=int(nsymbolstextfield.get())
    except:
        resultwindow=Toplevel(mainwindow)
        resultwindow.title("PASSWORD GENERATOR")
        resultwindow.geometry('900x500')
        label = Label(resultwindow, text="Error: Please enter valid numbers for length, \n alphabets, numbers, and symbols.", font=("Arial", 20),bg='black',fg='white')
        label.pack(expand=True, fill=BOTH)

    if length != nalphabets+nnumbers+nsymbols:
        resultwindow=Toplevel(mainwindow)
        resultwindow.title("PASSWORD GENERATOR")
        resultwindow.geometry('900x500')
        label = Label(resultwindow, text="Error: The specified length does not match the sum of alphabets, \n numbers, and symbols. Please try again.", font=("Arial", 20),bg='black',fg='white')
        label.pack(expand=True, fill=BOTH)
    else:
        password=[]
        for i in range(1,nalphabets+1):
            password += random.choice(alphabets)
        for i in range(1,nnumbers+1):
            password += random.choice(numbers)
        for i in range(1,nsymbols+1):
            password += random.choice(symbols) 

        random.shuffle(password)
        finalpassword = ""
        for i in password:
            finalpassword+=i
        resultwindow=Toplevel(mainwindow)
        resultwindow.title("PASSWORD GENERATOR")
        resultwindow.geometry('600x500') 
        label = Label(resultwindow, text="PASSWORD is  "+finalpassword, font=("Arial", 20),bg='black',fg='white')
        label.pack(expand=True, fill=BOTH)
        


generate=Button(
    text='Generate Password',
    font=('timesnewroman',15,'bold'),
    fg='white',
    bg='darkblue',
    command=generatepassword,
    
)
generate.pack(side=LEFT,padx=320,pady=50)



mainwindow.mainloop()