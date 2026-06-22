class User:
    def __init__(self, username: str, password:str):
        self.username = username
        self.password = password 
        
        
class Admin_User(User):
    def __init__(self):
        super().__init__()
        
        
class Employer(User):
    def __init__(self):
        super().__init__()
        
        
class Passenger(User):
    def __init__(self):
        super().__init__()
        
        
        
        
        
class Authentication:
    def __init__(self):
        self.admin = []
        self.employer = []    
        self.passenger = []
        
        
    def rigester(self, user) -> bool:
        if isinstance(user, Admin_User):
            self.admin.append(user)
            return True
        elif isinstance(user,Employer):
            self.employer.append(user)
            return True
        elif isinstance(user, Passenger):
            self.passenger.append(user)
            return True
        else:
            return False
            
        
        
    def login(self, username:str, password:str ) -> bool:
        for i in self.users :
            if username in i and password in i :
                return True      
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # self.users = []
        
        
        
        
    # def login(self, username:str, password:str ) -> bool:
    #     for i in self.users :
    #         if username in i and password in i :
    #             return True
            
    # def get_info(self) -> str :
    #     """
    #     show basic information 

    #     """
    #     return f"Name : {self.username} |  " 
             
        
