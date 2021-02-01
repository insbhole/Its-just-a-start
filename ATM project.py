'''Author - Aditya Yadav'''
import time
userpass = ""
usermoney = ""
a = None
print("**************************************************************")
print("*               WELCOME TO SOURCECODE BANK                   *")
print("**************************************************************")
while 1==1:
    try:
        k = int(input("Enter your account number: "))
        if k == 4024007144885554:
            userpass = "owwomxx"
            usermoney = 10000
        elif k == 4024007131522319:
            userpass = "ysuiean"
            usermoney = 12280
        elif k == 4539155087101907:
            userpass = "vqwzapq"
            usermoney = 14570
        elif k == 4321688577286442:
            userpass = "jwqmbym"
            usermoney = 9820
        elif k == 4556873122738511:
            userpass = "zcaumve"
            usermoney = 11240
        elif k == 5298333383584609:
            userpass = "jqzxtdd"
            usermoney = 17653
        elif k == 5126833109876393:
            userpass = "pzzpzgx"
            usermoney = 19876
        elif k == 5591089794132859:
            userpass = "uqwqaml"
            usermoney = 20000
        elif k == 5442962531198451:
            userpass = "iafxrsc"
            usermoney = 15567
        else:
            print("Account not available")
            continue
    except:
        print("Enter valid option")
        continue
    while 2==2:
        print("1. Withdraw\n2. Deposit\n3. Balance\n4. Pin change\n5. Get back to login page\n6. Mini statement\n7. Quit ")
        try:
            a = int(input("Enter your choice: "))
        except:
            print("Enter valid option")       
        if a == 1: #Withdraw
            try:
                b = str(input("Enter your password: "))
            except:
                print("Enter valid password")
                continue
            if b == userpass:
                try:
                    c = int(input("Enter the amount of money: "))
                except:
                    print("Enter valid amount")
                    time.sleep(3)
                    continue
                if c>usermoney:
                    print("Enter small amount")
                else:
                    print("You successfully withdrawl",c,"remaining money =",c-usermoney)
                    time.sleep(3)
            else:
                print("You entered wrong password, Try again")
                time.sleep(3)
                continue
        elif a == 2: #Deposit
            try:
                b = str(input("Enter your password: "))
            except:
                print("Enter valid password")
                continue
            if b == userpass:
                try:
                    c = int(input("Enter the amount of money: "))
                except:
                    print("Enter valid amount")
                    continue
                print("You successfully deposited",c,"balance =",c+usermoney)
                time.sleep(3)
            else:
                print("You entered wrong password, Try again")
                continue
        elif a == 3: #Balance
            try:
                b = str(input("Enter your password: "))
            except:
                print("Enter valid password")
                continue
            if b == userpass:
                print("Your balance is",usermoney)
                time.sleep(3)
        elif a == 4: #Change pin
            try:
                b = str(input("Enter your password: "))
            except:
                print("Enter valid password")
                continue
            if b == userpass:
                print("Remember! Password can only be in Alphabets")
                try:
                    v = str(input("Enter new pin: "))
                except:
                    print("Enter valid password")
                    continue
                userpass = v
                print("Your password have been successfully changed to",v)
                time.sleep(3)
            else:
                print("You entered wrong password, Try again")
                continue

        elif a == 6:
            try:
                b = str(input("Enter your password: "))
            except:
                print("Enter valid password")
                continue
            if b == userpass:
                print("Your account number is", k,"You have",usermoney,"available in your account")
                time.sleep(3)
        elif a == 5:
            break
    
        elif a == 7:
            print("Thank you for choosing us as your ATM. Please come back again:)")
    break 