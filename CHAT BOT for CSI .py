from tkinter import *
import random
screen = Tk()
screen.title("CSI - MINI PROJECT by VIDYARTH (20BCE0150)")
e = Entry(screen,font=('ariel',14,'bold'),   bg="powder blue",  width=65, borderwidth=8)
e.grid(row =0, column = 0,columnspan=5, padx = 6, pady =6)
good_comments = ['Everyday is a new day, BE HAPPY',"The most important thing is to enjoy your life — to be happy.",
                 "The purpose of our lives is to be happy, Don't worry its gonna be alright", "Wine is constant proof that God loves us and loves to see us happy.",
                 "Happiness is the best makeup.","Roll with the punches and enjoy every minute of it.", "The only thing that will make you happy is being happy with who you are.",
                 "Happiness comes in waves. It’ll find you again.", "When you love what you have, you have everything you need.",
                 "When it rains, look for rainbows. When it’s dark, look for stars."]

def b_click(b1):
    temp = e.get()
    e.delete(0,END)
    if temp.lower() =='.sad':
        word = random.choice(good_comments)
        e.insert(0,word)
    else:
        e.insert(0,"I am not trained for your question! Hope I will talk to you soon")
def b_clear(b2):
    e.delete(0,END)
b1 = Button(screen, text = 'SEND CHAT', font = ('ariel', 14,'bold'), bd=5,padx=6,pady=6, bg = 'silver', command = lambda :  b_click(1))
b2 = Button(screen, text = 'CLEAR CHAT', font = ('ariel', 14,'bold'), bd=5,padx=6,pady=6, bg = 'silver', command = lambda :  b_clear(1))
b1.grid(row = 0, column = 5)
b2.grid(row = 0, column = 6)
screen.mainloop()