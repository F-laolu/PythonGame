import tkinter
import random
import pickle


#Create list of various colours
coloursLi = ['Yellow', 'White', 'Grey', 'Black', 'Orange', 'Red', 'Pink', 'Purple', 'Brown', 'Green'] 
timer = 20 #set the initial program timer to 20seconds
scoreCount = 0 #initializes the score counter



#initializes the game function
def initialGame(event):
    if timer == 20:

        #displays the various options of colours available when enter key is pressed
        colabel.config(text=(coloursLi))

        #Begin the counter function
        counter()

    #Begin the function for random colour
    newColour()

#function to select random colour
def newColour():

    #including the global score count and timer variables
    global timer
    global scoreCount

    #while the game is running
    if timer > 0:
        
        #creating a new binary file
        col = open("colourrs.txt", "wb")
        #save the colours information in file
        pickle.dump(coloursLi, col)
        #close the file
        col.close()
        
        #activates text box
        colourEnt.focus_set()
        

        #condition for colour typed and font colour
        if colourEnt.get().lower() == coloursLi[1].lower():

            #score increment
            scoreCount += 1

        #empty text box
        colourEnt.delete (0, tkinter.END)
        #brings up new colour
        random.shuffle(coloursLi)

        #change text colour and colour font to random colour
        colourLabel.config(fg = str(coloursLi[1]), text = str(coloursLi[0]))

        #score update
        scoreGuide.config(text = "Your Score is: " + str(scoreCount))
        

#counter function
def counter():
    
    global timer

    #condition for when a game is still on
    if timer > 0:

        #timer is reduced
        timer -= 1

        #timer is updated
        timeGuide.config(text = "Time left is : " + str(timer) + "seconds")

        #timer starts again after 1 second
        timeGuide.after(1000, counter)


    





#code for second level which retains global score
timer2 = 14 #set the initial program timer to 20seconds

#initializes the game function
def beginGame(event):
    if timer2 == 14:

        #displays colours for level 2 when enter key is pressed
        colabel.config(text=(coloursLi))

        #Begin the counter function
        counter2()

    #Begin the function for random colour
    newColour2()

#function to select random colour
def newColour2():

    #including the global score count and timer variables
    global timer2
    global scoreCount

    #while the game is running
    if timer2 > 0:


        #creating a new binary file
        col = open("colourrs.txt", "wb")
        #save the colours information in file
        pickle.dump(coloursLi, col)
        #close the file
        col.close()

        #activates text box
        colourEnt.focus_set()

        #condition for colour typed and font colour
        if colourEnt.get().lower() == coloursLi[1].lower():

            #score increment
            scoreCount += 1

        #empty text box
        colourEnt.delete (0, tkinter.END)
        #brings up new colour
        random.shuffle(coloursLi)

        #change text colour and colour font to random colour
        colourLabel.config(fg = str(coloursLi[1]), text = str(coloursLi[0]))

        #score update
        scoreGuide.config(text = "Your Score is: " + str(scoreCount))

#counter function
def counter2():
    
    global timer2

    #condition for when a game is still on
    if timer2 > 0:

        #timer is reduced
        timer2 -= 1

        #timer is updated
        timeGuide.config(text = "Time left is : " + str(timer2) + "seconds")

        #timer starts again after 1 second
        timeGuide.after(1000, counter2)
        
#Level 2 GUI
def level_2():
        #Creating Level 2 interface GUI
        canvas = tkinter.Tk()
        canvas.configure(background="#c8a2c8")
        #The title of level 2 interface
        canvas.title("Brain Training Game!")
        #Interface size
        canvas.geometry("650x400+300+350")

        #Include label for program guide
        guide = tkinter.Label(canvas, text = "Welcome to Level 2 "
                                                        " Click on the initial interface and press the enter key to continue!", bg="#BEBAA7", fg="#000000", font="Times 14")
        guide.pack()

        #label for displaying the available colours
        colabel = tkinter.Label(canvas, text = "Colour options: " + str(coloursLi), bg='black', fg='#469A00')
        colabel.pack()

        #Include label for score count
        scoreGuide = tkinter.Label(canvas, text = "Press enter key to begin", bg="#BEBAA7", fg="#000000", font="Times 14")
        scoreGuide.pack()

        #Include label for colour display
        colourLabel = tkinter.Label(canvas, font = ('Sans', 50))
        colourLabel.pack() 

        #Create text box for entering colours
        colourEnt = tkinter.Entry(canvas)

        #Activate the program after pressing the enter key
        myInterface.bind('<Return>', beginGame)
        colourEnt.pack()

        #Stay on the entry box
        colourEnt.focus_set()

        #Include label for time count
        timeGuide = tkinter.Label(canvas, text = "Time: " +
                                str(timer2), bg="#BEBAA7", fg="#000000", font="Times 14")
        timeGuide.pack()
    

        #function for closing program
        def close_interface2 ():
            #command for ending program
            canvas.destroy ()

        #button to end program   
        button3 = tkinter.Button(canvas, text = "End program", bg='black', fg='#ffd700', command = close_interface2)
        button3.pack()
        


        










    
        


#Creating GUI for main interface 
myInterface = tkinter.Tk()
myInterface.configure(background="#B2BEB5")

#create size of the interface with axis
myInterface.geometry("650x400+300+350")

#program title
myInterface.title("Brain Training Game!")

#Include label for program guide
guide = tkinter.Label(myInterface, text = "Enter the font colour, "
                                                      "but not the word text given!", bg="#BEBAA7", fg="#000000", font="Times 14")
guide.pack()

#label for displaying the available colours
colabel = tkinter.Label(myInterface, text = "Colour options: " + str(coloursLi), bg='black', fg='#469A00')
colabel.pack()

#Include label for score count
scoreGuide = tkinter.Label(myInterface, text = "Press enter key to begin", bg="#BEBAA7", fg="#000000", font="Times 14")
scoreGuide.pack()

#Include label for colour display
colourLabel = tkinter.Label(myInterface, font = ('Sans', 50))
colourLabel.pack() 

#Create text box for entering colours
colourEnt = tkinter.Entry(myInterface)

#Activate the program after pressing the enter key
myInterface.bind('<Return>', initialGame)
colourEnt.pack()

#Stay on the entry box
colourEnt.focus_set()

#Include label for time count
timeGuide = tkinter.Label(myInterface, text = "Time: " +
			str(timer), bg="#BEBAA7", fg="#000000", font="Times 14")
timeGuide.pack()


#button that links to level 2 interface
button = tkinter.Button(myInterface, text="Click to begin Level 2", bg='black', fg='#469A00',
                              command=lambda: level_2())
button.pack()

#function for closing program
def close_interface ():
    #command for ending program
    myInterface.destroy ()

#button to end program   
button3 = tkinter.Button(myInterface, text = "End program", bg='black', fg='#ffd700', command = close_interface)
button3.pack()


#Call the GUI
myInterface.mainloop()
























      

