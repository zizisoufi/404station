class Panel:
    def __init__(self):
        pass
        
    def start(self):
        while True:
            print("\n Be 404 Station Khosh Omadi")
            print("1. Admin Panel")
            print("2. Employer")
            print("3. Passenger")
            print("4. Exit")

            i = input("Mikhay Koja Beri?")

            if i == "1":
                self.admin_login_panel()
            elif i == "2":
                pass
            elif i == "3":
                pass
            elif i == "4":
                print("Shab O RoozegaR Khosh")
                break
            else
                print("Dari Eshatebah Mizani Dadash")
        
        def admin_login_panel(self):
            while True:
                print("\n Admin Login")

                username = input("username: ")
                password = input("password: ")


                #pass auth class or db class 
                
                #check user and password validation

            # if validate succesfully
            self.admin_panel()

        def admin_panel(self):
            while True:
            print("\nPanel Modiriati")
            print("1. Add Emplouyer")
            print("2. Remove Employer")
            print("3. Show Employers")
            print("4. Back")

            i = input("Mikhay Koja Beri?")

            if i == "1":
                self.add_employer()
            elif i == "2":
                self.remove_employer()
            elif i == "3":
                self.show_employer()
            elif i == "4":
                return
            else
                print("Dari Eshatebah Mizani Dadash")

        def add_employer(self):
            print("\nAdd employer")

            username = input("Username: ")
            password = input("Password: ")

            #Check Validation and Append to employe list

        def remove_employer(self):
            username = input("Enter employer who we should remove")
            
            # chek if exist(if exist can be a method) remove from list

        def show_employer(self):
            if len() == 0:
                print("user nout found")
                return
            
            #for on employer

# we can write some metohd like if username exist and others 