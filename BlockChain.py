import hashlib
import time

import database_control


Database_name = "BGM_DataBase.db"
DataBase = database_control.DataBaseControll(Database_name)


class Block:

    def __init__(self , amount_ , target_wallet_ , main_wallet_ ):

        self.hash = ""
        self.prvious_hash = None
        self.amount = amount_
        self.target_wallet = target_wallet_
        self.main_wallet = main_wallet_
        self.time = time.strftime("%Y/%m/%d::%H:%M:%S")
        self.index = 0
        self.pr_index = 0
        self.count = 0

        self.GetIndex()
        self.GetPrHash()
        self.MakeHash()
        self.SaveToDataBase()
        self.BankContact()
    
    def GetIndex(self):

        Ex = "SELECT Count From Info"
        index_ = DataBase.get(Ex)
        
        print(index_)
        


        if index_ == []:

            self.index = 0
            self.pr_index = 0
            self.count = -1



        else: 

            index_ = index_[0][0]


            self.count = index_
            self.index = int(index_) + 1
            self.pr_index = self.count
           
     
        
    def GetPrHash(self):
        
        if self.pr_index != 0:

            Ex = f"SELECT hash FROM Block WHERE indexx = '{self.pr_index}' "

            print(DataBase.get(Ex))
            self.prvious_hash = DataBase.get(Ex)[0][0]

        else:

            self.prvious_hash = "First"


    def MakeHash(self):
        
        self.hash = hashlib.sha256(str(str(self.index)+str(self.amount)+self.prvious_hash+self.time+self.main_wallet+self.target_wallet).encode()).hexdigest()
        print(self.hash)


    def SaveToDataBase(self):
        

        if self.count == -1:
            Ex = "INSERT INTO Info VALUES('0')"

        else:
            Ex = f"""UPDATE Info SET Count = '{self.count+1}' WHERE Count = '{self.count}'"""

        DataBase.ex(Ex)

        Ex = f"INSERT INTO Block VALUES('{self.hash}' , '{self.prvious_hash}' , '{self.time}' , '{self.amount}' , '{self.target_wallet}' , '{self.main_wallet}' , '{self.index}') "
        DataBase.ex(Ex)


    def BankContact(self):


        Ex = f"SELECT money FROM Bank WHERE WalletAddr = '{self.main_wallet}' "

        first_money = DataBase.get(Ex)[0][0] - self.amount

        if first_money >= 0:

            Ex = f"UPDATE Bank SET money = '{first_money}' WHERE WalletAddr = '{self.main_wallet}'"

            DataBase.ex(Ex)



            Ex = f"SELECT money FROM Bank WHERE WalletAddr = '{self.target_wallet}'"

            two_money = DataBase.get(Ex)[0][0] + self.amount

            Ex = f"UPDATE Bank SET money = '{two_money}' WHERE WalletAddr = '{self.target_wallet}'"

            DataBase.ex(Ex)


            return True
        
        else:

            return False
    


Block(100 , "ahmad" , "ahoora" )
