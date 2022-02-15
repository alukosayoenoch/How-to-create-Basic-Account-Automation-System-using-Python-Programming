import time
import random
accNum=random.randint(99, 99999999999)

def main():
    #Creating objects and functions to get customer detail
    fname=str(input("\n Enter your first name: "))
    lname=str(input("\n Enter your last name: "))
    time.sleep(2)
    print("\n Welcome to coding101 autobanking platform ", fname, lname)
    time.sleep(2)
    print("\n Your autobanking email address is :", fname+'.'+lname+'@coding101.com')
    time.sleep(2)
    print("\n Your Account number is ", accNum)
    print("\n Account creation is successful...")

    #Creating Class BasicAccount
    class BasicAccount:
        def __init__(self):
            self.balance=0
            print("\n You are welcome to coding101 autobanking platform\n"
                  "\n Just a minutes....\n"
                  "\n Now redirecting you...\n"
                  "\n Connecting to our deposit and...\n"
                  "\n Withdrawal automation platform...\n")
            time.sleep(10)

    #Function to deposit amount
        def deposit(self):
            amount=float(input("\n Enter the amount to be deposit: "))
            self.balance+=amount
            print("\n Amount deposited is: ", '$',amount)
            time.sleep(2)

    #Function to Withdraw amount
        def withdraw(self):
            amount=float(input("\n Enter the amount to be withdrawn: "))
            if self.balance>=amount:
                self.balance-=amount
                print("\n You withdrew: ", '$',amount)
                time.sleep(2)
            else:
                print("\n Insufficient balance")
                time.sleep(2)

    #Function to display transaction details
        def display(self):
            print("\n Net available balance is: ", '$',self.balance)
            time.sleep(2)

    #Driver Codes/ Creating an object of class
    q=BasicAccount()
    #Calling function with the class object
    q.deposit()
    q.withdraw()
    q.display()
    main()
main()

          

