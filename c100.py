import random

number=random.randint(1,300000)

class Scammachine:
    def __init__(self,cardnum,pin):
        self.cardnum=cardnum
        self.pin=pin
    def balance(self):
        print("YOUR BALANCE IS "+str(number))
    def withdraw(self,amount):
        newamount=number-amount
        print("your balance was "+str(number)+" you have withdrawn amount "+str(amount)+" your remainning balace is "+str(newamount))

def main():
    cardnum=input("INSERT CARD NUMBER :)")
    pin=input("ENTER PIN NOW!!!")

    newuser=Scammachine(cardnum,pin)
    print("HOW CAN THIS ROBOT HELP you?!")
    print("1.Balance enquiry   2.withdrawl")
    activity=int(input("enter activity number"))
    if (activity==1):
        newuser.balance()
    elif(activity==2):
        amount=int(input("how much do you want to withdraw"))
        newuser.withdraw(amount)
    else:
        print("ENTER THE RIGHT NUMBER >:(")
main()
