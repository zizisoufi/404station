class Card:

    def __init__(self,card_number, exp_month, exp_year, password, cvv2):
        self._card_number = card_number
        self._exp_month = exp_month
        self._exp_year = exp_year
        self._password = password
        self._cvv2 = cvv2
        
    @property
    def card_number(self):
        return self.card
    
    @property
    def exp_month(self):
        return self.exp_month
    
    @property
    def card(self):
        return self.exp_year
    
    @property
    def exp_year(self):
        return self.exp_year
    
    @property
    def cvv2(self):
        return self.cvv2
    
   
    
    