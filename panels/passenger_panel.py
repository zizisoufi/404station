from classes.user import Passenger
from utilitys import backButton, print_file
from classes.ticket import Ticket
class PassengerPanel:
    def __init__(self, database, authentication):
        self.db = database
        self.auth = authentication      
        self.coocke = {}
    def passenger_panel(self):
        while True:
            print("\nPassenger Panel")
            print("1. Register")
            print("2. Login")
            print("3. Back")

            i = input("Mikhay koja beri? ").strip()

            if i == "1":
                self.register_passenger()
            elif i == "2":
                self.passenger_login_panel()
            elif i == "3":
                self.start()
            else:
                print("Dadash dari eshtebah mizani")
                         
    def passenger_login_panel(self):
        attempts = 1
        while attempts < 4: 
            print(f"\n--- Passenger Login (Attempt {attempts}/3) ---")
            
            username = input("Username: ").strip()
            if username.lower() == 'exit':
                return
            password = input("Password: ").strip()
            if username.lower() == 'exit':
                return
            
            passenger_auth = self.auth.login(username, password, "passenger")
            if passenger_auth["status"]:
                print(passenger_auth["message"])
                self.coocke["username"] = username
                self.passenger_dashboard()
            else:
                print(passenger_auth["message"])
                attempts += 1
                        
        print("Access Denied! Too many failed attempts.")
        return
    
    def register_passenger(self):
        print("\nPassenger Register")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        name = input("Name: ").strip()
        email = input("Email: ").strip()

        if backButton.back("dost dary hamina ro berizi? (Y/N)"):

            passenger = Passenger(username, password, name, email)
            passenger_auth = self.auth.register(passenger)
            
            if passenger_auth["status"]:
                print(passenger_auth["message"])
                self.passenger_panel()
            else:
                print(passenger_auth["message"])
                return
        else:
            if backButton.back("dost dari dobare bezani? (Y/n) "):
                self.register_passenger()
            else:
                self.passenger_panel()              
    def passenger_dashboard(self):
        while True:
            print("\n--- Passenger Dashboard ---")
            print("1. Buy Ticket")
            print("2. Update Profile")
            print("4. Back")

            i = input("Mikhay koja beri? ").strip()

            if i == "1":
                self.buy_ticket()
            elif i == "2":
                pass
            elif i == "3":
                return
            else:
                print("Dadash dari eshtebah mizani")

    def buy_ticket(self):
        print("\n--- BUY Panel ---")

        all_lines = self.db.read_all_data("lines")
        all_trains = self.db.read_all_data("trains")
        
        if len(all_lines) < 1:
            print("hanoz beliti baray frosh nist :)")
            self.passenger_dashboard()

        try:
            for line in all_lines:
                for train in all_trains:
                    if line.name == train.line:
                        is_printed = print_file.save_to_file("existed_trains.txt",destination=line.destination,train_name=train.name,ticket_cost=train.ticket_cost,train_capacity=train.capacity)
            if is_printed:
                print("The information of all existed trains in the existed_trains.txt file was saved.")
        except Exception as e:
            print(f"khataaaa!: {e}")
            self.passenger_dashboard()

        #check the train name is exist in existed train 
        all_train_names = [train.name for train in all_trains]
        train_name = input("esme ghatar mored nazar ra vared kon!: ")
        if not train_name in all_train_names:
            flag = True
            while flag:
                if backButton.back("ghatar ba in nam vojod nadarad mikhay dobare bezani? (Y/N): "):
                    train_name = input("esme ghatar mored nazar ra vared kon!: ")
                    if train_name in all_train_names:
                        flag = False
                else:
                    flag = False
                    self.passenger_dashboard()

        #find train name by the input of the user
        train = [train for train in all_trains if train.name == train_name]
        if int(train[0].capacity) < 1:
            print(f"ghatar {train[0].name} zarfiyati nadarad")
            self.passenger_dashboard()

        line = self.db.read("lines",train[0].line)

        try:
            count_ticket = int(input("che tedad ticket mikhay?: "))
            if int(train[0].capacity) - count_ticket < 0:
                print(f"ghatar {train[0].name} fahgat {train[0].capacity} ta zarfiyat dare")
                flag = True
                while flag:
                    if backButton.back(f"ghatar {count_ticket} ta zarfiyat nadarad mikhay tedad ro kamtar koni? (Y/N): "):
                        count_ticket = int(input("che tedad ticket mikhay?: "))
                        if not int(train[0].capacity) - count_ticket < 0:
                            flag = False
                    else:
                        flag = False
                        self.passenger_dashboard()
                
            self.db.update_data("trains",train[0].id,"capacity",int(train[0].capacity)-count_ticket)
            try:

                ticket = Ticket(username=self.coocke["username"],train_name=train[0].name,origin=line.origin,destination=line.destination,ticket_cost=train[0].ticket_cost,amount=count_ticket)
            except Exception as e:
                print(f"khataaa: {e}")
                self.passenger_dashboard()
            
            #here payment should implement

            is_printed = print_file.save_to_file("ticket.txt",username=ticket.username,train_name=ticket.train_name,origin=ticket.origin,destination=ticket.destination,ticket_cost=ticket.ticket_cost,count_ticket=ticket.amount,data=ticket.time)
            if is_printed:
                print("your ticket has successfuley been created")
                self.passenger_dashboard()
            else:
                print("We had a problem when creating the ticket.")
                self.passenger_dashboard()

        except Exception as e:
            print(f"khataaa: {e}")
            self.passenger_dashboard()
        
