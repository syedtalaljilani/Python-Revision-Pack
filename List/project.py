welcome_msg = '''
Select The Following Options 
1.View Data
2.Insert Data
3.Remove Data
4.Modify Data
5.Search Data
'''

from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()
def db_connect():
    mongodb_uri = os.getenv('MONGO_URI')
    client = MongoClient(mongodb_uri)
    print(client.list_database_names())
    print('kk')

print(db_connect())

'''print(welcome_msg)
user_choice = abs(int(input('Enter Your Option')))
data = []
match (user_choice):
    case 1:
        if len(data) == 0:
            print('No Data Avaiable')
        else:
            print(data)
    case 2:
          user_data = input('Enter Your Data')
          data.append(user_data)
          print(data)
    case 3:
         user_data = input('Enter Data You Want to Remove')
         for i in range(data):
              if data[i] is user_data:
                    data.remove(user_data)
              else:
                   print('No Data Found') '''