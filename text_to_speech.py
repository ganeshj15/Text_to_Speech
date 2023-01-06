
from gtts import gTTS
from tkinter import *
from playsound import playsound
import os

window = Tk()
window.geometry('350x300')
window.resizable(0,0)
window.title('GDJ_Text to Speech')
window.configure(bg='cyan')

Label(window, text="Text to Speech", font='arial 20 bold', bg='cyan', fg='orange').pack()
Label(window, text="GDJ", font='arial 10 bold', bg='cyan', fg='red').pack(side='bottom')

msg = StringVar()
Label(window, text="Enter Text", font='arial 15 bold', bg='cyan').place(x=20, y=60)
entry_field = Entry(window, textvariable=msg, width=50)
entry_field.place(x=20, y=100,height=25)

def text_to_speech():
    message = entry_field.get()
    speech = gTTS(text=message)
    speech.save('audio.mp3')
    playsound('audio.mp3')
    os.remove('audio.mp3')

def Exit():
    window.destroy()

def Reset():
    msg.set("")

# Buttons
Button(window,text='PLAY',font= 'arial 15 bold', command=text_to_speech,bg='orange', width=4).place(x=25, y=140)
Button(window, font= 'arial 15 bold', text='EXIT', width=4, command=Exit, bg='OrangeRed1').place(x=100, y=140)
Button(window, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset,bg='orange').place(x=175 , y = 140)

window.mainloop()