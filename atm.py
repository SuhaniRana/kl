class Atm:
    def __init__(self,card,pin):
        self.card = card
        self.pin = pin
    def check_balance(self):
        print("Your balance is 30,000 dollars")
    def withdraw(self,withdrawl):
        new_amount = 30,000 - withdrawl
        print("You have withdrawn: "+str(withdrawl)+". Your new total is: " + str(new_amount))
    
    def main(self):
        card_number = input("Enter card number:- ")
        pin_number = input("enter pin number:- ")
        user = Atm(card_number,pin_number) 
        print("choose your option ")
        print("1. Balance inquiry    2. withdrawl")
        option = input(int("enter activity number:- "))

        if(option == 1):
            user.check_balance()
        elif(option == 2):
            amount = int((input("enter amount to withdraw:-")))
            user.withdraw(amount)
        else:
            print("Please enter a valid option")


print(.withdraw(20))

        
