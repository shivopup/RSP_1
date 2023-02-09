from tkinter import *
from tkinter import messagebox
import random
variation = ['rock', 'scissors', 'paper']
pcount = 0
mcount = 0


def clickrock():
    global pcount, mcount
    pchoice = 'rock'
    mchoice = random.choice(variation)

    if mchoice == 'rock':
        print('Draw')
        messagebox.showinfo('Draw', f'You-{pchoice}\nOpponent-{mchoice}\nNo winners!')
    elif mchoice == 'scissors':
        print('Win!')
        messagebox.showinfo('Congratz!', f'You-{pchoice}\nOpponent-{mchoice}\nYou won!')
        pcount += 1
        print(pcount, mcount)
    else:
        print('Lost')
        messagebox.showinfo('You lost', f'You-{pchoice}\nOpponent-{mchoice}\nYou lost!')
        mcount += 1
        print(pcount, mcount)
    count.configure(text=f'{pcount}:{mcount}')

def clickscissors():
    global pcount, mcount
    pchoice = 'scissors'
    mchoice = random.choice(variation)

    if mchoice == 'scissors':
        print('Draw')
        messagebox.showinfo('Draw', f'You-{pchoice}\nOpponent-{mchoice}\nNo winners!')
    elif mchoice == 'paper':
        print('Win!')
        messagebox.showinfo('Congratz!', f'You-{pchoice}\nOpponent-{mchoice}\nYou won!')
        pcount += 1
    else:
        print('Lost')
        messagebox.showinfo('You lost', f'You-{pchoice}\nOpponent-{mchoice}\nYou lost!')
        mcount += 1
    count.configure(text=f'{pcount}:{mcount}')

def clickpaper():
    global pcount, mcount
    pchoice = 'paper'
    mchoice = random.choice(variation)

    if mchoice == 'paper':
        print('Dra')
        messagebox.showinfo('Draw', f'You-{pchoice}\nOpponent-{mchoice}\nNo winners!')
    elif mchoice == 'rock':
        print('Win!')
        messagebox.showinfo('Congratz!', f'You-{pchoice}\nOpponent-{mchoice}\nYou won!')
        pcount += 1
    else:
        print('Lost')
        messagebox.showinfo('You lost', f'You-{pchoice}\nOpponent-{mchoice}\nYou lost!')
        mcount += 1
    count.configure(text=f'{pcount}:{mcount}')

window = Tk()
window.title("Rock, scissors and paper!")
window.geometry('500x250')
lbl = Label(window, text="Let's Go!!", font=('Arial', 20))
lbl.grid(column=0, row=0)
count = Label(window, text='You count', font=('Arial', 20))
count.grid(column=0, row=3)
rock = Button(window, text="Rock!", width=10, height=2, command=clickrock)
rock.grid(column=1, row=2)
scissors = Button(window, text="Scissors!", width=10, height=2, command=clickscissors)
scissors.grid(column=2, row=2)
paper = Button(window, text="Paper!", width=10, height=2, command=clickpaper)
paper.grid(column=3, row=2)
window.mainloop()

