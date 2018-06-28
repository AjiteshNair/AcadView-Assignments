from tkinter import *

#Question 1
print("\n\nQ1.\n")

dictionary = {'Batman': '10', 'Goku': '9000', 'iron man': '9', 'hulk': '20'}
root = Tk()

frame = Frame(root)
frame.pack()

scroll = Scrollbar(frame)
scroll.pack(fill=Y, side=RIGHT)
dictx = Listbox(frame, yscrollcommand=scroll.set)

for key in dictionary:
    dictx.insert(END, '{}'.format(key))
    
dictx.pack(side=LEFT)
scroll.config(command = dictx.yview)

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

#Question 2
print("\n\nQ2.\n")

def add():
    
    dictionary.update({hero.get(): level.get()})
    
    for key in dictionary.keys():
        print(key)
        
    i = key
    dictx.insert(END, i)


text = Label(frame,text="Hero name and its level: ")
text.pack()

hero = Entry(frame, text="Superhero")
level = Entry(frame, text="Power level:")
hero.pack()
level.pack()

button = Button(frame, text="ADD HERO", command=add)
button.pack()

root.mainloop()

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
