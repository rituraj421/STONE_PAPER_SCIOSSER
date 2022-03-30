#stone paper sciosser game
from tkinter import*
from PIL import Image, ImageTk
from random import randint

root = Tk()
root.title("Stone Paper Sciosser")
root.configure(background="#808080")

stone_img = ImageTk.PhotoImage(Image.open("stone-Me.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-Me.png"))
Sciosser_img = ImageTk.PhotoImage(Image.open("Sciosser-Me.png"))
stone_img_her = ImageTk.PhotoImage(Image.open("stone.png"))
paper_img_her = ImageTk.PhotoImage(Image.open("paper.png"))
Sciosser_img_her = ImageTk.PhotoImage(Image.open("Sciosser.png"))


me_label = Label(root,image=Sciosser_img, bg="#808080")
her_label = Label(root,image=Sciosser_img_her, bg="#808080")
her_label.grid(row=1,column=0)
me_label.grid(row=1,column=4)



meScore = Label(root,text=0,font=100,bg="#808080", fg="black")
herScore = Label(root,text=0,font=100,bg="#808080", fg="black")
herScore.grid(row=1, column=1)
meScore.grid(row=1, column=3)


her_indicator = Label(root,font=50,text="HER",bg="#808080", fg="black").grid(row=0,column=1)
me_indicator = Label(root,font=50,text="ME",bg="#808080", fg="black").grid(row=0,column=3)





msg = Label(root, font=50,bg="#808080", fg="Black").grid(row=3,column=2)


#message updation
def updateMessage(X):
    msg['text'] = X

#     #update players score
# def updateMeScore():
#         score = int(meScore["text"])
#         score += 1
#         meScore["text"] = str[score]



# def updateHerScore():
#         score = int(herScore["text"])
#         score += 1
#         herScore["text"] = str[score]
    
# #who is winner
# def checkWinner(me, her):
#     if me == her:
#         updateMessage("yeah!!, It's a Tie🙂 Play again")
#     elif me == "stone":
#         if her == "paper":
#             updateMessage("You lose1!😞, she won!!🙂")
#             updateHerScore()
#         else:
#             updateMessage("You Win!!🙂")
#             updateMeScore()
#     elif me == "paper":
#         if her == "Sciosser":
#             updateMessage("You lose1!😞, she won!!🙂")
#             updateHerScore()
#         else:
#             updateMessage("You Win!!🙂")
#             updateMeScore()
#     elif me == "Sciosser":
#         if her == "stone":
#             updateMessage("You lose1!😞, she won!!🙂")
#             updateHerScore()
#         else:
#             updateMessage("You Win!!🙂")
#             updateMeScore()

#     else:
#         pass

# #choise

# choices = ["stone", "paper", "Sciosser"]
def updateChoice(X):

# #Her Choice
#     herChoice = choices[randint(0,2)]      
#     if herChoice == "STONE":
#         her_label.configure(image=stone_img_her)
#     elif herChoice == "PAPER":
#         her_label.configure(image=paper_img_her)
#     else:
#         her_label.configure(image=Sciosser_img_her)





    if X == "stone":
        me_label.configure(image=stone_img)
    elif X == "paper":
        me_label.configure(image=paper_img)
    else:
        me_label.configure(image=Sciosser_img)


# checkWinner(X, herScore)

stone = Button(root,width=20,height=2,text="STONE", bg="#FF0000", fg="Black",command = lambda:updateChoice("stone")).grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="PAPER", bg="#FF0000", fg="Black",command = lambda:updateChoice("paper")).grid(row=2,column=2)
Sciosser = Button(root,width=20,height=2,text="SCIOSSER", bg="#FF0000", fg="Black",command = lambda:updateChoice("Sciosser")).grid(row=2,column=3)




root.mainloop()

# ritu's code start(previous one)
# def whoWin(Her, You):
#     #If both the inputs are same
#     if You == Her:
#         return None


#     elif Her == 's':
#         if You == 'p':
#             return True
#         elif You == 'k':
#             return False 


#     elif Her == 'p':
#         if You == 'k':
#             return True
#         elif You == 's':
#             return False


#     elif Her == 'k':
#         if You == 's':
#             return True
#         elif You == 'p':
#             return False

# print("Her turn: Stone(s) Paper(p) or Sciosser(k)?") # here k == sciosser(कैंची),(kainchee)
# randNo = random.randint(1, 3)
# if randNo == 1:
#     Her = 's'
# elif randNo == 2:
#     Her = 'p'
# elif randNo == 3:
#     Her = 'k'

# You = input("Your Turn: Stone(s) Paper(p) or Sciosser(k)?")
# a = whoWin(Her, You)

# print(f"Her chose {Her}")
# print(f"You chose {You}")

# if a == None:
#     print("It's a tie!, Play again")
# elif a:
#     print("congrats You(me) win!!")
# else:
#     print("She won!!")

    # YOU HAVE TO ENTER INPUT AS 'S', 'P', OR 'K' ANY ONE OF THEM
    # ritu's code end here(previous one)

