from tkinter import *
import requests



class window:

    def __init__(self):

        self.url_api = "http://127.0.0.1:5000"
        self.MainPage()

    def MakeWindow(self , title , geometry):


        self.window = Tk()

        self.window.title(title)

        self.window.resizable(False , False)

        self.window.geometry(geometry)

        

    def CreateAccount(self):

        self.MakeWindow("New Account" , "400x500")

        nameWallet = StringVar()

        def NewAccount():

            name = nameWallet.get()

            req = requests.get(self.url_api+"/create")

            print(str(req.content).split("#"))
        

        Label(self.window , text="Your Wallet Name:").place(x=140 , y=60)

        Entry(self.window , width= 40 , border=3, textvariable=nameWallet).place(x=73 , y= 80)

        Button(self.window,width=30,text="Submit",command=NewAccount).place(x=90 , y=130)


        self.window.mainloop()


    def MainPage(self):

        def login():
            
            self.window.destroy()

        def new_account():

            self.window.destroy()

            self.CreateAccount()

        self.MakeWindow("BGM Account" , "400x400")


        Button(self.window , text= "Create Account" , width= 30 , border=5 ,command= new_account).place(x=90 , y=100)

        Button(self.window , text= "Login" , width= 30 , border=5 , command=login ).place(x=90 , y=150)

        self.window.mainloop()


        
window_ = window()