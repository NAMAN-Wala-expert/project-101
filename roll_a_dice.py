import random
seconds = 1000
response = input("write y for yes and n for no")
no = random.randint(1,6)
 
while (response != "n"):
    no = random.randint(1,6)
    if  response != "n" :
        print(no)
        response = input("write y for yes and n for exit")
    else:
            print("thank you for using this app")

 





