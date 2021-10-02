import tkinter as tk
import tkinter.messagebox



def clickMe():
    tkinter.messagebox.showinfo(title='提示', message = '玩遊戲')


window = tk.Tk()

window.title('我愛free fire+Pubg絕地求生M')

window.geometry('300x300')



label = tk.Label(window,text='玩遊戲',bg='#000',fg= '#FFF')
label.pack()

entry = tk.Entry(window,width = 40)
entry.pack()

button = tk.Button(window,text = '玩遊戲',command = clickMe)
button.pack()




window.mainloop()