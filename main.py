from tkinter import *
import random


def next_trun(row, column):

    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+"-turn"))

            elif check_winner() is True:
                label.config(text=(players[0]+"-wins"))

            elif check_winner() == "Tie":
                label.config(text=("Match Drawn!"))

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+"-turn"))

            elif check_winner() is True:
                label.config(text=(players[1]+"-wins"))

            elif check_winner() == "Tie":
                label.config(text=("Match Drawn!"))



def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
#for diogonal:
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")

        return "Tie"

    else:
        return False


def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1


    if spaces == 0:
        return False
    else:
        return True


def new_game():

    global player

    player = random.choice(players)

    label.config(text=player+"-turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="gray")

window = Tk()
window.title("Tic~Tac~Toe")
players = ["@","$"]
player = random.choice(players)
buttons = [[0,0,0],    #[(0,0),(0,1),(0,2)]
           [0,0,0],    #[(1,0),(1,1),(1,2)]
           [0,0,0]]    #[(2,0),(2,1),(2,2)]


label = Label(text= player + "-turn", font=('consolas',40), width=16, height=2)
label.pack(side="top")
label.config(bg="salmon")


reset_button = Button(text="RESTART", font=('consolas',20), command=new_game)
reset_button.pack(side="bottom")
reset_button.config(text="RASTART", bg="sky blue")


frame = Frame(window)
frame.pack()



for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40), width=3, height=1,
                                      command= lambda row=row, column=column: next_trun(row,column))
        buttons[row][column].grid(row=row,column=column)
        buttons[row][column].config(text="", bg="gray")


window.mainloop()