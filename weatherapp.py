from tkinter import *
from tkinter import messagebox
import requests


mainwindow = Tk()
mainwindow.title('WEATHER APP')
mainwindow.geometry('700x450')
mainwindow.config(bg='orchid')


title_label = Label(mainwindow, text='WEATHER APP', fg='purple', bg='white', font=('SERIF', 30,'bold'), )
title_label.pack(pady=80,padx=0)

frame=Frame(
    mainwindow,
        padx=0,
        pady=0,
        bg='orchid'
)
frame.pack(expand=True)


citylabel=Label(
    frame,
    text="Enter City : ",
    font=('timesnewroman', 20,'bold'),
    bg='white',
    fg='purple')
citylabel.grid(row=1,column=1)
citytextfield=Entry(frame,font=('timesnewroman', 23),
                    bg='white',
                    fg='purple'
                   )
citytextfield.grid(row=1,column=2,pady=5)

def findweather():
    city = citytextfield.get()
    API_key = 'd411f9623a61d78186e6507881cb7b3d'
    weather=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={API_key}")
    if weather.json()['cod'] =='404':
        messagebox.showinfo("ERROR ",'No City found !')
    else:
        wdata = weather.json()['weather'][0]['main']
        tdata = round(weather.json()['main']['temp'])
        tdata = round((tdata-32)//1.8)

        message = f"The weather in {city} is: {wdata}\nThe temperature in {city} is: {tdata}\u00b0C"

        resultwindow=Toplevel(mainwindow)
        resultwindow.title("Weather Information")
        resultwindow.geometry('400x300')
        label = Label(resultwindow, text=message, font=("Arial", 14))
        label.pack(expand=True, fill=BOTH)
           
        

find=Button(
    text='Find Weather',
    font=('timesnewroman',15,'bold'),
    fg='purple',
    bg='white',
    command=findweather,
)
find.pack(side=LEFT,padx=220,pady=50)


mainwindow.mainloop()