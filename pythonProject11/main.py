finish = 0 
total = 0
while finish == 0:
       user = input('Please type the integer number you would like to add. If you do not want to add any more numbers type "Q": ')
       if user == "Q":
            finish = 1
            print(total)
       else:
            total = total + int(user)