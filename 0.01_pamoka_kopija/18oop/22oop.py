from tkinter import *
window = Tk()
window.title('Pirmas kartas...')
window.geometry('700x500')
window.iconbitmap('pav.ico')
#ivesties laukai
ivestis1 = Entry(window)
ivestis2 = Entry(window)
#ivesties talpinimas
ivestis1.pack(side=LEFT)
ivestis2.pack(side=RIGHT)

myg1 = Button(window, text='Spausk1!', command='')
myg1.pack()

window.mainloop()