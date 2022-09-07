from tkinter import *

# GUI
root = Tk()
root.title("Chatbot")
root.geometry("400x500")
root.resizable(width=FALSE, height=FALSE)

# Send function
def send():
	send = "You -> " + messageWindow.get()
	chatWindow.insert(END, "\n" + send)

	user = messageWindow.get().lower()

	if (user == "hello"):
		chatWindow.insert(END, "\n" + "Bot -> Hi there, how can I help?")

	elif (user == "hi" or user == "hii" or user == "hiiii"):
		chatWindow.insert(END, "\n" + "Bot -> Hi there, what can I do for you?")

	elif (user == "how are you"):
		chatWindow.insert(END, "\n" + "Bot -> fine! and you")

	elif (user == "fine" or user == "i am good" or user == "i am doing good"):
		chatWindow.insert(END, "\n" + "Bot -> Great! how can I help you.")

	elif (user == "Thanks" or user == "Thank you" or user == "now its my time"):
		chatWindow.insert(END, "\n" + "Bot -> My pleasure !")

	elif (user == "What do you sell " or user == "What kinds of items are there" or user == "have you something"):
		chatWindow.insert(END, "\n" + "Bot -> We have coffee and tea")

	elif (user == "Tell me a joke" or user == "Tell me something funny" or user == "crack a funny line"):
		chatWindow.insert(END, "\n" + "Bot -> i am Out of stock, i wiil tel you some day  ")

	elif (user == "Goodbye" or user == "See you later" or user == "see yaa"):
		chatWindow.insert(END, "\n" + "Bot -> Have a nice day!")

	elif (user == "bye" or user == "See you later" or user == "see yaa"):
		chatWindow.insert(END, "\n" + "Bot -> Have a nice day!")
	elif (user == "good morning" or user == "good afternoon" or user == "good night"):
		chatWindow.insert(END, "\n" + "Bot ->You also have a very "+user)
	else:
		chatWindow.insert(END, "\n" + "Bot -> Sorry! I didn't got you")


	messageWindow.delete(0, END)


chatWindow = Text(root, bd=1, bg="#70c7b4",  width = "50" , height="8", font=("Arial", 15), foreground="black")
chatWindow.place(x=6,y=6, height=385, width=370)

messageWindow = Entry(root, bd=0, bg="#70c7b4", width="30", font=("Arial", 15), foreground="black")
messageWindow.place(x=128, y=400, height=88, width=260)

scrollbar = Scrollbar(root,bg="#DAF7A6", command=chatWindow.yview, cursor="arrow")
scrollbar.place(x=375, y=5, height=385)

send= Button(root, text="Send", width="12", height=5, bd=0, bg="#FF5733", activebackground="#00bfff", foreground='#ffffff', font=("Arial", 12), command=send)
send.place(x=6, y=400, height=88)


root.mainloop()
