

import tkinter as tk

window = tk.Tk()

window.title("我愛free fire+Pubg絕地求生M")

window.geometry("300x500")

menuBar = tk.Menu(window)

filrMenu = tk.Menu(menuBar,tearoff=False)

filrMenu.add_command(label="麥克雞塊")

filrMenu.add_command(label="麥香雞")

submenu= tk.Menu(menuBar,tearoff=False)

submenu.add_command(label="30元")

submenu.add_command(label="40元")

filmenu.add_cascade(label="vhhvh",menu=submenu)

menuBar.add_cascade(label="麥當勞",filmenu)

window.config(menu=menuBar)

window.mainloop()