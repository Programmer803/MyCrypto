

import sqlite3
import time
import hashlib


class DataBaseControll:

     def __init__(self , Database_name):



          self.conn = sqlite3.connect(Database_name , check_same_thread=False)

          self.act = self.conn.cursor()

     def ex(self , data):
          
               
               self.act.execute(data)

               self.conn.commit()
               
               
     def get(self , ex):
               

               
               self.act.execute(ex)
               data = self.act.fetchall()
               self.conn.commit()
               
               return data
     
     def AddAccunt(self , walletAddr , publicKey):
             
             walletAddr = hashlib.sha256(str(walletAddr).encode()).hexdigest()

             
             Ex = f"INSERT INTO Bank VALUES('{walletAddr}','{time.strftime("%Y/%m/%d::%H:%M:%S")}','0','0','{publicKey}')"

             self.ex(Ex)