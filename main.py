from tkinter import*
root= Tk()

root.title("Trini Ride Taxi Service")
root.geometry("400x400")
root.configure(background="white")

adminlogin_label = Label(root, text="Administrator Login")
adminlogin_label.grid(row=1, column=1, padx=10, pady=10)

#Label Widgets
Email= Label(root, text="Email:", bg="orange")
Password= Label(root, text="Password:", bg="orange")

#Size of Widgets
Email.grid(row=2, column=0, padx=10, pady=10, sticky=W)
Password.grid(row=3, column=0, padx=10, pady=10, sticky=W)

emaillvalue= StringVar
passwordvalue= StringVar

#Entry Widgets
emailentry=Entry(root, textvariable=emaillvalue)
passwordentry=Entry(root, textvariable=passwordvalue, show="*")

#Size of Entry Widgets
emailentry.grid(row=2, column=1, padx=10, pady=10, sticky=W)
passwordentry.grid(row=3, column=1, padx=10, pady=10, sticky=W)

#Popup Box
import tkinter.messagebox

def onClick():
    tkinter.messagebox.showinfo ("Trini Ride Taxi Service", "Login Successful")

#Create Button Confirm

button1 = Button(root, text="Login", command=onClick, height=1, width=5, padx=10, pady=10, bg="green")
button1.grid(row=7, column=1, columnspan=1)

#Popup Box
import tkinter.messagebox

def onClick():
    tkinter.messagebox.showinfo ("Trini Ride Taxi Service", "Cancel Successful")

#Create Buttons Cancel

button2 = Button(root, text="Cancel", command=onClick, height=1, width=5, padx=10, pady=10, bg="red")
button2.grid(row=7, column=2, columnspan=1)

root.mainloop()