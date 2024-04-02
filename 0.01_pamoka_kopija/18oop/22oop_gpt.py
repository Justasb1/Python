from tkinter import *

window = Tk()
window.title('Pirmas kartas...')
window.geometry('700x500')

# Attempt to set the window icon
try:
    window.iconbitmap('pav.ico')
except Exception as e:
    print("Error setting window icon:", e)

# Input fields
ivestis1 = Entry(window)
ivestis2 = Entry(window)

# Input field placement
ivestis1.pack(side=LEFT)
ivestis2.pack(side=RIGHT)

# Button
myg1 = Button(window, text='Spausk1!', command='')
myg1.pack()

window.mainloop()
