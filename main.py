from tkinter import *

root = Tk()

root.geometry('250x228')
root.resizable(False, False)
root.title('Узнай цвет')

color_label = Label(root, text='')
color_label.pack(fill=X)

color_entry = Entry(root, bd=4, justify=CENTER)
color_entry.insert(0, '')
color_entry.pack(fill=X)


def add_red():
    color_label['text'] = 'красный'
    color_entry.delete(0, END)
    color_entry.insert(0, '#ff0000')


btn_red = Button(root, bg='#ff0000', command=add_red)
btn_red.pack(fill=X)


def add_orange():
    color_label['text'] = 'оранжевый'
    color_entry.delete(0, END)
    color_entry.insert(0, '#ff7d00')


btn_orange = Button(root, bg='#ff7d00', command=add_orange)
btn_orange.pack(fill=X)


def add_yellow():
    color_label['text'] = 'желтый'
    color_entry.delete(0, END)
    color_entry.insert(0, '#ffff00')


btn_yeloww = Button(root, bg='#ffff00', command=add_yellow)
btn_yeloww.pack(fill=X)


def add_green():
    color_label['text'] = 'зеленый'
    color_entry.delete(0, END)
    color_entry.insert(0, '#00ff00')


btn_green = Button(root, bg='#00ff00', command=add_green)
btn_green.pack(fill=X)


def add_blues():
    color_label['text'] = 'голубой'
    color_entry.delete(0, END)
    color_entry.insert(0, '#007dff')


btn_blues = Button(root, bg='#007dff', command=add_blues)
btn_blues.pack(fill=X)


def add_blue():
    color_label['text'] = 'синий'
    color_entry.delete(0, END)
    color_entry.insert(0, '#0000ff')


btn_blue = Button(root, bg='#0000ff', command=add_blue)
btn_blue.pack(fill=X)


def add_rouse():
    color_label['text'] = 'фиолетовый'
    color_entry.delete(0, END)
    color_entry.insert(0, '#7d00ff')


btn_rouse = Button(root, bg='#7d00ff', command=add_rouse)
btn_rouse.pack(fill=X)


root.mainloop()
