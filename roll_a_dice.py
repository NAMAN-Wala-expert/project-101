import random
seconds = 1000
response = input("write y for yes and n for no")
no = random.randint(1,6)
 
while (response != "n"):
    no = random.randint(1,6)
    if  response != "n" :
        print(no)
        if  no == 1:
         print("[     ]")
         print("[  0  ]")
         print("[     ]")
        elif no == 2:
         print("[     ]")
         print("[ 0 0 ]")
         print("[     ]")
        elif no == 3:
         print("[  0  ]")
         print("[  0  ]")
         print("[  0  ]")
        elif no == 4:
         print("[0   0]")
         print("[     ]")
         print("[0   0]")
        elif no == 5:         
         print("[0   0]")
         print("[  0  ]")
         print("[0   0]")
        else :      
         print("[0   0]")
         print("[0   0]")
         print("[0   0]")
         
        response = input("write y for yes and n for exit")
    else:
            print("thank you for using this app")
    
         
         


 





