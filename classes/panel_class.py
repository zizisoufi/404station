class Panel:
    def __init__(self, menu):
        self.menu = menu
        
    def get_menu(self):
        return self.menu
    
    
class Start_Panel(Panel):
    def __init__(self, menu:dict ) :
        super().__init__(menu)
        
class Admin_Panel(Panel):
    def __init__(self, menu:dict ) :
        super().__init__(menu)
        
        
class Employer_Panel(Panel):
    def __init__(self, menu:dict ) :
        super().__init__(menu)
          
    
class Passenger_Panel(Panel):
    def __init__(self, menu:dict ) :
        super().__init__(menu)
        

class Buy_Panel(Panel):
    def __init__(self, menu:dict ) :
        super().__init__(menu) 
    