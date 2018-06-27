
from tkinter import *

#Question 1
print("\n\nQ1.\n")

r = Tk()
r.title('Question 1')           #for title of the window made

text_output = Label(r , text='Hello world !')               #to output text on the window
text_output.pack()                                          #to pack the text on the window

button = Button(r, text='EXIT', width = 30, command=r.destroy)          #for exit button
button.pack()                                                           #to pack the exit button

#Question 2 hereon

def disp_text():                                                #funtion to start a new window for question 2 
    r2 = Tk()
    r2.title('Question 2 now')
    
    text_output = Label(r2,text='QUESTION 2 TAKING OVER! , There is nowhere left to hide ! >:D ')
    text_output.pack()

    exit_button = Button(r2, text='EXIT Q2?' , width=30 , command=r2.destroy)
    exit_button.pack()

    r2.mainloop()

button_q2 = Button(r, text='Click here for Q2 ', width=30 , command=disp_text)              #button to call the funtion disp_text
button_q2.pack()

r.mainloop()                    #looping the window

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

#Question 3
print("\n\nQ3.\n")

root = Tk()

root.title("Question 3")

disp = Label(root, text='You wanna know my secret identity? ')              #for text
disp.pack()

def change_text():
    disp.config(text="I'm Batman")                                      #changing the text and packing it

button = Button(root, text='well , do you?', command=change_text )
button.pack()                                               


exit_button = Button(root, text='EXIT', width=30, command=root.destroy)
exit_button.pack()


root.mainloop()


#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

#Question 4
print("\n\nQ4.\n")

root = Tk()

root.title("Question 4")

input_text = Entry(root)
input_text.pack()


input_text.insert(INSERT, "Enter: ")             #to take input 

def display():
    print("Entered Text is : ",input_text.get()[7:])            #to display entered text

button = Button(root, text='Print entered text', command=display)   #calls the diplay function
button.pack()


exit_button = Button(root, text='EXIT',width=30, command=root.destroy)      #EXIT BUTTON 
exit_button.pack()

root.mainloop()             #looping until exit or X is pressed

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
