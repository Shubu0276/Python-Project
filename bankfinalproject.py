class Bank:
    # Constructor
    def __init__(self):
        self.regilist = {}  # changes
        self.validation = []  #
        self.logged_in_user = None
        self.statement = {}

    # Create Account = name, age, phone, location, aadhar, pan
    def Create_Acc(self):
        while True:
            print()
            self.name = input("Enter Name: ")
            if self.name.isdigit():
                print()
                print("Please Enter Valid Name")
                print()
                continue
            else:
                while True:
                            self.age = int(input("Enter Age: "))
                            if self.age >= 100 or self.age <= 0:
                                print()
                                print("Please Enter Valid Age")
                                print()
                            else:
                                while (True):
                                    self.mail = input("Enter Email-Id: ")
                                    if '@' and ".com" not in self.mail:
                                        print("\nPlease Enter valid Mail which include '@' and '.com'")
                                        print()
                    
                                    else:
                                        while True:
                                            self.phone = int(input("Enter Phone No.: "))
                                            le = len(str(self.phone))
                                            if self.phone not in self.validation:
                                                if le != 10:
                                                    print()
                                                    print("Please Enter valid 10 Digit Phone Number")
                                                    print()
                                                else:
                                                    self.validation.append(self.phone)
                                                    while True:
                                                        self.loc = input("Enter Locality: ")
                                                        if self.loc.isdigit():
                                                            print()
                                                            print("Please Enter Valid Location")
                                                            print()
                                                        else:
                                                            while True:
                                                                self.aadhar = int(input("Enter AadharNo.: "))
                                                                if self.aadhar not in self.validation:
                                                                    if len(str(self.aadhar)) != 16:
                                                                        print()
                                                                        print("Please Enter 16 Digit Valid Aadhar No.")
                                                                        print()
                                                                    else:
                                                                        self.validation.append(self.aadhar)
                                                                        while True:
                                                                            self.pan = input("Enter Pan No.: ")
                                                                            le1 = self.pan[0:5]
                                                                            le2 = self.pan[9:10]
                                                                            le3 = self.pan[5:9]
                                                                            if self.pan not in self.validation:
                                                                                if self.pan.isupper() == True and le1.isalpha() == True and le2.isalpha() == True and le3.isdigit() == True and len(self.pan) == 10:
                                                                                    while True:
                                                                                        self.validation.append(self.pan)
                                                                                        self.Pin = int(input("Create 4 Digit Pin: "))
                                                                                        self.regilist.update({self.name: [self.Pin, self.pan, self.phone, self.aadhar, self.loc, self.mail, self.age]})  # changes
                                                                                        if len(str(self.Pin)) == 4:
                                                                                            while True:
                                                                                                self.pin1 = int(input("Please Confirm Pin: "))
                                                                                                if self.pin1 == self.Pin:
                                                                                                    print()
                                                                                                    print(" x-x-x-x    Account Created Succesfully    x-x-x-x ")
                                                                                                    print()
                                                                                                    print(" x-x-x-x-x-x ",self.name,"Welcome To SBI    x-x-x-x-x-x ")
                                                                                                    print()
                                                                                                    self.validation.append(self.Pin)
                                                                                                    return
                                                                                                else:
                                                                                                    print("\nPIN not matched")
                                                                                        else:
                                                                                            print()
                                                                                            print("Enter Only 4 Digit Pin")
                                                                                            print()
                                                                                            return
                                                                                        
                                                                            
                                                                            else:
                                                                                print("Account with This Pan No. Already Exist")
                                                                else:
                                                                    print("\nAccount With This Aadhar No. Already Exist")
                                            else:
                                                print("\nAccount With This Number Already Exist")
    
    # Login Account = deposit, withdraw, balance, edit, information, bank statement, delete acc
    def Login_Acc(self):
        self.balance = 100  # Starting balance
        attempts = 3

        a = input("\nEnter Name: ")

        if a in self.regilist:  # changes
            while attempts > 0:
                b = int(input("Enter your PIN: "))
                if b == self.regilist[a][0]:  # changes
                    self.logged_in_user = a
                    print("\nLogin successful.")
                    break
                else:
                    attempts -= 1
                    print("\nInvalid PIN. Attempts left: ",attempts) #f

            if attempts == 0:
                print("\nYou have exceeded the maximum number of attempts. Your card has been blocked.")
                return

            while True:
                print()
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Delete")
                print("5. Edit")
                print("6. Info")
                print("7. View Statement")
                print("8. Exit")

                choice = input("\nEnter your choice: ")

                if choice == "1":
                    print()
                    print(" >>>>>>>>>>>>>>> Deposite Amount <<<<<<<<<<<<<<<  ")
                    amount = float(input("\nEnter the amount to deposit: "))
                    self.depo(amount)

                elif choice == "2":
                    print()
                    print(" >>>>>>>>>>>>>>> Withdraw Amount <<<<<<<<<<<<<<< ")
                    amount = float(input("\nEnter the amount to withdraw: "))
                    self.withdraw(amount)

                elif choice == "3":
                    print()
                    print(" >>>>>>>>>>>>>>>> Balance Information <<<<<<<<<<<<<<< ")
                    print("\nCurrent balance: ",self.balance)

                elif choice == "4":
                    print()
                    print(" >>>>>>>>>>>>>>> Delete Account <<<<<<<<<<<<<<< ")
                    self.delete_account()
                    return

                elif choice == "5":
                    print()
                    print(" >>>>>>>>>>>>>> Edit Information <<<<<<<<<<<<<<< ")
                    self.edit_account()

                elif choice == "6":
                    print()
                    print(" >>>>>>>>>>>>>>> Account Information <<<<<<<<<<<<<<< ")
                    print()
                    self.info_account()

                elif choice == "7":
                    print()
                    self.view_statement()

                elif choice == "8":
                    print()
                    print("x-x-x-x Thank You Visit again x-x-x-x")
                    print()
                    break

                else:
                    print("Invalid choice. Please try again.")

        else:
            print("No Account Found")
    
    # Admin Login
    def admin(self):
        
        while True:
            adname = input("Enter username : ")
            if adname == "shubhada":
                adpass = input("Enter Password : ")
                if adpass == "0276":
                    print("\nAdmin Login Successfull")
                    while True:
                        
                        print("\nHello Admin")
                        print("1. View All Accounts")
                        print("2. Close an Account")
                        print("3. View Bank Statements")
                        print("4. Generate Reports")
                        print("5. Logout")
                        admin_choice = input("\nEnter your choice: ")

                        if admin_choice == "1":
                            self.view_all_accounts()

                        elif admin_choice == "2":
                            self.close_account()

                        elif admin_choice == "3":
                            self.view_bank_statements()

                        elif admin_choice == "4":
                            self.generate_reports()

                        elif admin_choice == "5":
                            print("\nLogged out from admin account.")
                            return

                        else:
                            print("\nInvalid choice. Please try again.")
                else:
                    print("\nIncorrect Password")
                    print()
            else:
                print("\nIncorrect Username")
                print()
                return
               
    # close Account by Admin
    def close_account(self):
        name_to_close = input("\nEnter Name to close the account: ")
        if name_to_close in self.regilist:
            confirm = input("\nAre you sure you want to close this account? (yes/no): ").lower()
            if confirm == "yes":
                deleted_account = self.regilist[name_to_close]
                self.validation.remove(deleted_account[2])
                self.validation.remove(deleted_account[3])
                self.validation.remove(deleted_account[1])
                del self.regilist[name_to_close]
                print("\nAccount closed successfully.")
            else:
                print("\nAccount closure canceled.")
        else:
            print("\nAccount not found.")
    
    # View All Accounts by Admin
    def view_all_accounts(self):
        print("\n >>>>>>>>>>>>>>> All Registered Accounts <<<<<<<<<<<<<<< ")
        if self.regilist:
            for name, details in self.regilist.items():
                print(f"\nName: \t\t {name}")
                print("Age: \t\t", details[6])
                print("Location: \t", details[4])
                print("Phone Number: \t", details[2])
                print("Email-Id: \t", details[5])
                print("Aadhar Number: \t", details[3])
                print("Pan Number: \t", details[1])
                print("PIN: \t\t", details[0])
        else:
            print("No accounts found.")
    
    # View Bank Statement by Admin
    def view_bank_statements(self):
        print("\n >>>>>>>>>>>>>>> Bank Statements <<<<<<<<<<<<<<< ")
        if self.statement:
            for user, transactions in self.statement.items():
                print(f"\nName: {user}")
                print("Transactions:")
                               
                for transaction in transactions:
                    print(transaction)
        else:
            print("No bank statements found.")
    
    # Reports by admin
    def generate_reports(self):
        print("\n >>>>>>>>>>>>>>> Generate Reports <<<<<<<<<<<<<<< ")
        if self.regilist:
            total_accounts = len(self.regilist)
            # total_balance = sum(account_info[0] for account_info in self.regilist.values())
            print("Total Number of Accounts:", total_accounts)
            # print("Total Balance in the Bank:", total_balance)
        else:
            print("No accounts found.")
    
    # Deposite by User
    def depo(self, amount):
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
        else:
            self.balance += amount
            print("Deposited", amount, "New balance is: ",self.balance)
            self.statement.setdefault(self.logged_in_user, []).append(f"Deposited: {amount}")
    
    # Withdraw by User
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
        elif self.balance >= amount:
            self.balance -= amount
            print("Withdrawn", amount, "New balance is", self.balance)
            self.statement.setdefault(self.logged_in_user, []).append(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance.")
    
    # Edit = loc, pin, phone by User
    def edit_account(self):
        self.validation.append(self.edit_account)
        if self.name in self.regilist:
            print()
            print("1. Edit Location")
            print("2. Edit PIN")
            print("3. Edit Phone Number")
            print("4. Back")
            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.changeloc()

            elif choice == "2":
                self.changepin()

            elif choice == "3":
                self.changephone()

            elif choice == "4":
                return

            else:
                print("Invalid choice. Please try again.")

        else:
            print("\nAccount not found.")
    
    # Change location by User
    def changeloc(self):
        new_location = input("Enter new Location: ")
        self.regilist[self.name][4] = new_location
        print("Location updated successfully.")
    
    # Change pin by User
    def changepin(self):
        pin = input("\nEnter previous PIN number :")
        if pin.isdigit():
            if int(pin) == self.regilist.get(self.name)[0]:
                new = input("Enter new PIN : ")
                if new.isdigit() and len(new) == 4:
                    new1 = input("Re-enter the new PIN : ")
                    if new == new1:
                        self.regilist[self.name][0] = int(new)
                        print("\nPin Changed sucessfully")
                        print()
                    else:
                        print("Pin Not Matched")
                        print()
                else:
                    print("Enter 4 Digit Pin Only")
                    print()
            else:
                print("Invalid PIN")
                print()
        else:
            print("Please enter PIN in digits only..!")
            print()
    
    # Change phone by User
    def changephone(self):
        new_phone = int(input("Enter new Phone Number: "))
        if len(str(new_phone)) == 10:
            if self.phone in self.regilist[self.name]:
                self.regilist[self.name][2] = new_phone
                print("Phone Number updated successfully.")
            else:
                self.regilist[self.name].update({self.phone: new_phone})
        else:
            print("Invalid phone number. Please enter a valid 10-digit phone number.")
    
    # Delete acc by User
    def delete_account(self):
        name_to_delete = input("\nEnter Name: ")
        if name_to_delete in self.regilist:
            confirm = input("\nAre you sure you want to delete your account? (yes/no): ").lower()
            if confirm == "yes":
                deleted_account = self.regilist[name_to_delete]
                self.validation.remove(deleted_account[2])
                self.validation.remove(deleted_account[3])
                self.validation.remove(deleted_account[1])
                del self.regilist[name_to_delete]
                print("\nAccount deleted successfully.")
            else:
                print("\nAccount deletion canceled.")
        else:
            print("\nAccount not found.")
    
    # Account Information by User
    def info_account(self):
        if self.logged_in_user in self.regilist:
            account_info = self.regilist[self.logged_in_user]
            print("Name: \t\t", self.logged_in_user)
            print("Age: \t\t", account_info[6])
            print("Location: \t", account_info[4])
            print("Phone Number: \t", account_info[2])
            print("Email-Id: \t", account_info[5])
            print("Aadhar Number: \t", account_info[3])
            print("Pan Number: \t", account_info[1])
            print("PIN: \t\t", account_info[0])
            
            
        else:
            print("\nAccount not found.")
    
    # Bank Statement by User
    def view_statement(self):
        if self.logged_in_user in self.statement:
            print()
            print(" >>>>>>>>>>>>>>> Your Transaction History <<<<<<<<<<<<<<<")
            print()
            for transaction in self.statement[self.logged_in_user]:
                print(transaction)
        else:
            print("No transaction history found.")
    
    # Show
    def home(self):
        print("\n----->|  Welcome to SBI  |<-----")
        while True:
            print("....................")
            print("1. Create Account \n2. Login Account \n3. Admin Login")
            print("....................")
            choice = input("Enter your choice : ")
            if choice == "1":
                print()
                print(" >>>>>>>>>>>>>>> Create Account <<<<<<<<<<<<<<< ")
                self.Create_Acc()
            elif choice == "2":
                print()
                print(" >>>>>>>>>>>>>>>> Login Page <<<<<<<<<<<<<<< ")
                self.Login_Acc()

            elif choice == "3":
                print()
                print(" >>>>>>>>>>>>>>>> Admin Login <<<<<<<<<<<<<<< ")
                print()
                self.admin()

            else:
                print("\nInvalid choice. Please try again.")
    
# Assigning Object
obj = Bank()

# Calling Object
obj.home()

