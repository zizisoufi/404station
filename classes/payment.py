from classes.Card import Card
from BANK import API
from classes.user import Passenger

class PaymentService:
    def __init__(self) -> None:
        self.bank = API()
    
    def show_my_cards(self, passenger):
        print("\nMy Cards")
        if not passenger.cards:
            print("No saved cards yet")
            return    
    
    def _read_amount(self):
        try:
            amount = int(input("amount: ").strip())
            if amount <= 0:
                print("amount not be 0 ")
                return None
            return amount
        except ValueError:
            ("amount not valid")
            return None
         
    def _read_new_card(self):
        try:
            card_number = input("Card Number: ").strip()
            exp_month = int(input("Card Number: ").strip())
            exp_year = int(input("Card Number: ").strip())
            password = input("Card Number: ").strip()
            cvv2 = input("Card Number: ").strip()
            
            
            return Card(card_number, exp_month, exp_year, password, cvv2)
        except ValueError:
            print("invalid card")
            return None
        
        
    def _get_card_for_payment(self, passenger):
        if passenger.cards:
            print("1. use saved card")
            print("2. add new card")
            choice = input("choose: ").strip()
            
            if choice == "1":
                return self._choose_saved_Card(passenger), False
            if choice == "2":
                return self._read_new_card(), True
            
            print("invalid choice")
            return None, False
        
        
    def _choose_saved_Card(self, passenger):
        if not passenger.cards:
            print("you dont have any card")
            return None
        self.show_my_card(passenger)
        
        try:
            choice = int(input("choose card number: ").strip())
            if 1 <= choice <= len(passenger.cards):
                return passenger.cards[choice -1]
        except ValueError:
            pass
        print("invalid card choice")
    
    def charge_wallet(self, passenger):
        print("\nCharge Walllet")
        
        try:
            amount = int(input("Cheghadr charge mikhaye?"))
            
            if amount <= 0:
                print("mablagh vared shode bayad bishtar az 0 bashad")
                return
        
            card_number = input("shomare cartet chande?").strip()
            exp_month = int(input("mahe enghezaye kartet chiye?").strip())
            exp_year = int(input("sale enghezaye kartet chiye?").strip())
            password = input("password kartet chiye?").strip()
            cvv2 = input("cvv2 enghezaye kartet chiye?").strip()
            
            payment = self.bank.pay(card_number, exp_month, exp_year, password, cvv2, amount)

            passenger.wallet += amount

            print("wallet charged succesfully")
            print("payment ID:", payment)
        
        except ValueError as error:
            print("payment failed:", error)
    
    def pay_from_wallet(self,amount,passenger):
        if passenger.wallet < amount:
            print("your balance is not enough")
            return False 
        passenger.wallet -= amount
    
        
    def show_wallet_balance(self, passenger):
        print("\nWallet Balance")
        print(f"your walllet amount is {passenger.wallet}")
    
    def show_my_card(self, passenger):
        return passenger.cards
        
    
         
            
            
