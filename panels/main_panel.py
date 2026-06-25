from classes.user import Admin_User, Employer, Passenger #, Authentication
from services.authentication import Authentication
from database.database import DataBase

class MainPanel:
    def __init__(self):
        self.db   = DataBase()
        self.auth = Authentication(database=self.db)
        #Default admin username and password
        admin = Admin_User("admin", "admin")
        # self.auth.rigester(admin)
        self.db.create_DI(admin, "admins")

    def start(self):
        while True:
            print("\nBe 404 Station Khosh Omadi")
            print("1. Admin Panel")
            print("2. Employer")
            print("3. Passenger")
            print("4. Exit")

            choice = input("Mikhay Koja Beri? ")

            if choice == "1":
                self.admin_login_panel()
            elif choice == "2":
                self.employer_login_panel()
            elif choice == "3":
                self.passenger_panel()
            elif choice == "4":
                print("Shab O RoozegaR Khosh")
                exit()
            else:
                print("Dari Eshatebah Mizani Dadash")
