import mysql.connector
import matplotlib.pyplot as plt
from tabulate import tabulate
from decimal import Decimal


class Bank:
   
    # constructor
    def __init__(self):
    
        self.a=mysql.connector.connect(host='localhost',username='root',password='',database='projectdb')
        self.b = self.a.cursor()
        self.a.commit()
        print("Connected")
    # by user
    def Create_Acc(self):

        
        while (True):
            print()
            self.name = input("Enter Name: ")
            for i in self.name:
                if type(i)==int:
            # if self.name.isdigit():
                # print()
                 print("Please Enter Valid Name")
                 print()
                continue
            
            else:
                while (True):
                    self.age = int(input("Enter Age: "))
                    if self.age >= 100 or self.age <= 0:
                        print()
                        print("Please Enter Valid Age")
                        print()

                    else:
                        while(True):
                            self.phone = int(input(("Enter Phone No.: ")))
                            le = len(str(self.phone))
                            if le != 10:
                                    print()
                                    print("Please Enter valid 10 Digit Phone Number")
                                    print()
                            else: 
                                while(True):
                                    self.loc = input("Enter Locality: " )
                                    if self.loc.isdigit():
                                        print()
                                        print("Please Enter Valid Location")
                                        print()
                                    
                                    else:
                                        while (True):
                                                self.aadhar = int(input("Enter AadharNo.: "))
                                            # while True:
                                                self.checkaadhar()
                                                if len(str(self.aadhar)) != 12:
                                                    print()
                                                    print("Please Enter 12 Digit Valid Aadhar No.")
                                                    print()
                                                # continue
                                                
                                                else:
                                                    while (True):
                                                            self.pan = input("Enter Pan No.: ")
                                                            le1 = self.pan[0:5]
                                                            le2 = self.pan[9:10]
                                                            le3 = self.pan[5:9]
                                                            self.checkpan()
                                                        
                                                            
                                                            
                                                            
                                                            if self.pan.isupper() == True and le1.isalpha() == True and le2.isalpha() == True and le3.isdigit() == True and len(self.pan) == 10:
                                                                while (True):
                                                                    self.Pin = int(input("Create 4 Digit Pin: "))
                                                                    if len(str(self.Pin)) == 4 :
                                                                        self.insertdb()

                                                                        print()
                                                                        print(" >>>>>>>>>>>>>>>> Account Created Succesfully <<<<<<<<<<<<<<< ")
                                                                        print()
                                                                        print(" >>>>>>>>>>>>>>>> ",self.name,"Welcome To SBI <<<<<<<<<<<<<<< ")
                                                                        print()
                                                                        return 
                                                            
                                                                    else:
                                                                        print()
                                                                        print("Enter Only 4 Digit Pin")
                                                                        print()

                                                            else:
                                                                print()
                                                                print("Please Enter 10 Digit pan No. in Valid Format")
                                                                print()
                                                                 # by user     
    # by user
    def Login_Acc(self):
        
        self.balance = 100  # Starting balance
        attempts = 3  
        
        n = input("\nEnter Name: ")
        self.b.execute("select name from bnk where name = %s",[n])
        ab = self.b.fetchall()
        
        if ab:
                while attempts > 0:
                    b = int(input("Enter your PIN: "))
                    self.b.execute("select pin from bnk where name = %s",[n])
                    ab1 = self.b.fetchone()
                    if ab1:
                        ab2,=ab1
                        if ab2 == b:
                            self.name = n
                            print("\nLogin successful.")
                            # self.retrieve_balance()
                            self.choices()
                            
                        else:
                            attempts -=1
                            print(f"Invalid PIN. Attempts left: {attempts}")

                if attempts == 0:
                    print("\nYou have exceeded the maximum number of attempts. Your card has been blocked.")
                    return
        else:
            print("Account not found")
    # by user
    def get_logged_in_user_data(self):
        try:
            user_data = {}

            query_transaction_history = "SELECT * FROM transaction WHERE user_id = (SELECT aadhar FROM bnk WHERE name = %s)"
            self.b.execute(query_transaction_history, (self.name,))
            result_transaction_history = self.b.fetchall()

            if result_transaction_history:
                transactions = []
                for transaction in result_transaction_history:
                    transaction_data = {
                        "Transaction_ID": transaction[0],
                        "User_ID": transaction[1],
                        "Amount": transaction[2],
                        "Transaction_Type": transaction[3],
                        "Transaction_Date": transaction[4]
                    }
                    transactions.append(transaction_data)
                user_data["Transaction_History"] = transactions
            else:
                print("No transaction history found")
            return user_data
        except mysql.connector.Error as err:
            print("Error fetching user data:", err)
            return None
    # by user
    def choices(self):
                        while True:
                            print()
                            print("1. Deposit")
                            print("2. Withdraw")
                            print("3. Check Balance")
                            print("4. Delete")
                            print("5. Edit")
                            print("6. Info")
                            print("7. View Statement")
                            print("8. Logout")

                            choice = input("\nEnter your choice: ")

                            if choice == "1":
                                print()
                                print(" >>>>>>>>>>>>>>>> Deposite Amount <<<<<<<<<<<<<<< ")
                                amount = Decimal(input("\nEnter the amount to deposit: "))
                                if amount <= 0:
                                    print("Invalid amount. Please enter a positive value.")
                                else:
                                    self.deposit(amount)

                            elif choice == "2":
                                print()
                                print(" >>>>>>>>>>>>>>>> Withdraw Amount <<<<<<<<<<<<<<< ")
                                amount = Decimal(input("\nEnter the amount to withdraw: "))
                                if amount <= 0:
                                    print("Invalid amount. Please enter a positive value.")
                                else:
                                    self.withdraw(amount)
                                

                            elif choice == "3":
                                print()
                                self.retrieve_balance()
                                print(" >>>>>>>>>>>>>>>> Balance Information <<<<<<<<<<<<<<< ")
                                print(f"\nCurrent balance: {self.balance}")

                            elif choice == "4":
                        
                                 self.delete_account()  
                                 return 
                        
                            elif choice == "5":
                                print()
                                print(" >>>>>>>>>>>>>>>> Edit Information <<<<<<<<<<<<<<< ")
                                self.edit_account()

                            elif choice == "6":
                       
                               self.info_account()

                            elif choice == "7":
                                print()
                                print(" >>>>>>>>>>>>>>>> Transaction History <<<<<<<<<<<<<<< ")
                                print()
                                user_data = self.get_logged_in_user_data()
                                if user_data and "Transaction_History" in user_data:
                                    transactions = user_data["Transaction_History"]
                                    # print("\n >>>>>>>>>>>>>>> Your Transaction History <<<<<<<<<<<<<<<\n")
                                    for transaction in transactions:
                                        print(f"Transaction ID: {transaction['Transaction_ID']}")
                                        print(f"User ID: {transaction['User_ID']}")
                                        print(f"Amount: {transaction['Amount']}")
                                        print(f"Transaction Type: {transaction['Transaction_Type']}")
                                        print(f"Transaction Date: {transaction['Transaction_Date']}")
                                        print("----------------------------------------------------------")
                                else:
                                    print("No transaction history found.")
                                # self.view_statement()
                                
                            elif choice == "8":
                                 print()
                                 print(" >>>>>>>>>>>>>>>> Thank You Visit Again <<<<<<<<<<<<<<<")
                                 print()
                                 self.home()

                            else:
                                print("Invalid choice. Please try again.")
    # by user
    def retrieve_balance(self):
      try:
        query = "SELECT balance FROM bnk WHERE name = %s"
        self.b.execute(query, (self.name,))
        result = self.b.fetchone()

        if result:
            self.balance = result[0]
            # print("Your account balance:", self.balance)  # Update self.balance with the retrieved balance
        else:
            print("Account Not Found")
      except mysql.connector.Error as err:
          print("error fetching balance: ",err)
    # by user
    def checkaadhar(self): 
        while True:
            check_aadhar_query = "SELECT COUNT(*) FROM bnk WHERE aadhar = %s"
            self.b.execute(check_aadhar_query, (self.aadhar,))
            result = self.b.fetchone()
            
            if result[0] > 0:
                    print("Aadhar number already exists. Please enter a different Aadhar number.")
                    self.aadhar = int(input("Enter AadharNo.: "))
            else:
                    break   
    # by user    
    def checkpan(self):
        while (True):
            check_pan_query = "SELECT COUNT(*) FROM bnk WHERE pan = %s"
            self.b.execute(check_pan_query, (self.pan,))
            result = self.b.fetchone()

            if result[0] > 0:
                print("PAN number already exists. Please enter a different PAN number.")
                self.pan = input("Enter Pan No.: ")
            else:
                break        
    # by user
    def deposit(self, amount):
        try:
            update_query = "UPDATE bnk SET balance = balance + %s WHERE name = %s"
            self.b.execute(update_query, (amount, self.name))
        
            
            transaction_query = "INSERT INTO transaction (user_id, amount, transaction_type) VALUES ((SELECT aadhar FROM bnk WHERE name = %s), %s, 'Deposit')"
            self.b.execute(transaction_query, (self.name, amount))
            
            self.a.commit()
            self.retrieve_balance()
            
            print(f"Deposited {amount}. New balance: {self.balance}")
        
        except mysql.connector.Error as err:
            print("Error depositing amount:", err)
    # by user
    def withdraw(self, amount):
        try:
            if self.balance >= amount:
                update_query = "UPDATE bnk SET balance = balance -  %s WHERE name = %s"
                self.b.execute(update_query, (amount, self.name))
                
                transaction_query = "INSERT INTO transaction (user_id, amount, transaction_type) VALUES ((SELECT aadhar FROM bnk WHERE name = %s), %s, 'Withdrawal')"
                self.b.execute(transaction_query, (self.name, amount))
                
                self.a.commit()
                self.retrieve_balance()
                
                print(f"Withdrawn {amount}. New balance: {self.balance}")
            else:
                print("Insufficient balance for withdrawal.")
        
        except mysql.connector.Error as err:
            print("Error Withdrawing Amount", err)
    # by user
    def view_statement(self):
        try:
            user_data = self.get_logged_in_user_data()
            if user_data and "Transaction_History" in user_data:
                transactions = user_data["Transaction_History"]
                if transactions:
                    print("\n >>>>>>>>>>>>>>> Your Transaction History <<<<<<<<<<<<<<<\n")
                    for transaction in transactions:
                    
                        print(f"Transaction ID: {transaction['Transaction_ID']}")
                        print(f"User ID: {transaction['User_ID']}")
                        print(f"Amount: {transaction['Amount']}")
                        print(f"Transaction Type: {transaction['Transaction_Type']}")
                        print(f"Transaction Date: {transaction['Transaction_Date']}")
                        print("----------------------------------------------------------")
                else:
                    print("No transaction history found.")
            else:
                print("No transaction history found.")
        except mysql.connector.Error as err:
            print("Error fetching transaction history:", err)
    # by user
    def info_account(self):
        print()
        print("  >>>>>>>>>>>>>>>>    Account Information   <<<<<<<<<<<<<<< ")
        print()
        query = "SELECT name, location, phone, aadhar, pan, pin FROM bnk WHERE name = %s"
        self.b.execute(query, (self.name,))
        result = self.b.fetchone()

        if result:
            print(f"Name: \t\t {result[0]}")
            print(f"Location: \t {result[1]}")
            print(f"Phone Number: \t {result[2]}")
            print(f"Aadhar Number: \t {result[3]}")
            print(f"Pan Number: \t {result[4]}")
            print(f"PIN: \t\t {result[5]}")
        else:
            print("Account not found")
    # by user
    def edit_account(self):
        
            print()
            print("1. Edit Location")
            print("2. Edit PIN")
            print("3. Edit Phone Number")
            print("4. Back")
            choice = input("\nEnter your choice: ")

            if choice == "1":
                new_location = input("Enter new Location: ")
                
                update_query = "UPDATE bnk SET location = %s WHERE name = %s"
                self.b.execute(update_query, (new_location, self.name))
                self.a.commit()
                print("Location updated successfully.")

            elif choice == "2":
                new_pin = input("Enter new 4 Digit PIN: ")
                if len(new_pin) == 4 and new_pin.isdigit():
                    update_query = "UPDATE bnk SET pin = %s WHERE name = %s"
                    self.b.execute(update_query, (new_pin, self.name))
                    self.a.commit()
                    print("PIN updated successfully.")
                
                else:
                    print("Invalid PIN. Please enter a valid 4-digit PIN.")

            elif choice == "3":
                new_phone = int(input("Enter new Phone Number: "))
                if len(str(new_phone)) == 10:
                    update_query = "UPDATE bnk SET phone = %s WHERE name = %s"
                    self.b.execute(update_query, (new_phone, self.name))
                    self.a.commit()
                    print("Phone Number updated successfully.")
                
                else:
                    print("Invalid phone number. Please enter a valid 10-digit phone number.")

            elif choice == "4":
                        return

            else:
                        print("Invalid choice. Please try again.")       
    # by user
    def delete_account(self):
       
            name_to_delete = input("\nEnter Name: ")
            confirm = input("\nAre you sure you want to delete your account? (yes/no): ").lower()

            if confirm == "yes":
                try:
        # Find the user's ID based on the provided name
                    select_user_query = "SELECT aadhar FROM bnk WHERE name = %s"
                    self.b.execute(select_user_query, (name_to_delete,))
                    user_id = self.b.fetchone()

                    if user_id:
                        user_id = user_id[0]  # Extract the user ID from the result

            # Check if there are related records in the transaction table
                        check_transaction_query = "SELECT * FROM transaction WHERE user_id = %s"
                        self.b.execute(check_transaction_query, (user_id,))
                        related_records = self.b.fetchall()

                        if related_records:
                # Delete related records in the transaction table first
                            delete_transaction_query = "DELETE FROM transaction WHERE user_id = %s"
                            self.b.execute(delete_transaction_query, (user_id,))
                            self.a.commit()  # Commit the transaction

            # Proceed with deleting the user's account from the bnk table
                        delete_bnk_query = "DELETE FROM bnk WHERE aadhar = %s"
                        self.b.execute(delete_bnk_query, (user_id,))
                        self.a.commit()  # Commit the transaction

                        print("\nAccount deleted successfully.")
                        self.home()
                    else:
                        print("\nUser not found.")
                    

                except Exception as e:
                    print("Error deleting account:", e)

            else:
                print("\nAccount deletion canceled.")  
    # by admin                    
    def admin(self):
        
        while True:
            adname = input("Enter username : ")
            if adname == "shubhada":
                adpass = input("Enter Password : ")
                if adpass == "0276":
                    print("\nAdmin Login Successfull")
                    while True:
                        
                        print("\nHello Admin")
                        print()
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
                            self.home()
                            return

                else:
                    print("\nIncorrect Password")
                    print()
            else:
                print("\nIncorrect Username")
                print()
                return
    # by admin            
    def view_all_accounts(self):
        print("\n >>>>>>>>>>>>>>> All Registered Accounts <<<<<<<<<<<<<<< ")
        try:
            self.b.execute("SELECT * FROM bnk")
            all_accounts = self.b.fetchall()

            if all_accounts:
            
                for account in all_accounts:
                    print(f"\nName: \t\t {account[0]}")  
                    print("Age: \t\t", account[1])  
                    print("Location: \t", account[2]) 
                    print("Phone Number: \t", account[3])
                    print("Aadhar Number: \t", account[4])
                    print("Pan Number: \t", account[5])
                    print("PIN: \t\t", account[6])
                    print("----------------------------------------------------------")

            else:
                print("No accounts found.")
        except mysql.connector.Error as err:
            print("Error:", err)
    # by admin
    def view_bank_statements(self):
        try:
            query = "SELECT * FROM transaction"
            self.b.execute(query)
            transactions = self.b.fetchall()
            print("\n >>>>>>>>>>>>>>> Bank Statements <<<<<<<<<<<<<<<\n")

            if transactions:
                headers = ["Transaction ID", "User ID", "Amount", "Transaction Type", "Transaction Date"]
                table_data = [[
                transaction[0],  # Transaction ID
                transaction[1],  # User ID
                transaction[2],  # Amount
                transaction[3],  # Transaction Type
                transaction[4],  # Transaction Date
                ] for transaction in transactions]

                print("\n >>>>>>>>>>>>>>> Bank Statements <<<<<<<<<<<<<<<\n")
                print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
                # for transaction in transactions:
                #     print(f"Transaction ID: {transaction[0]}")
                #     print(f"User ID: {transaction[1]}")
                #     print(f"Amount: {transaction[2]}")
                #     print(f"Transaction Type: {transaction[3]}")
                #     print(f"Transaction Date: {transaction[4]}")
                #     print("----------------------------------------------------------")
            else:
                print("No bank statements found.")
        except mysql.connector.Error as err:
            print("Error fetching bank statements:", err)
    # by admin
    def generate_reports(self):
        print("\n >>>>>>>>>>>>>>> Generate Reports <<<<<<<<<<<<<<< ")
        print("1. No. of Accounts")
        print("2. Graphs")
        print("3. Exit")

        while True:
            print()
            admin_choice1 = input("Enter your Choice: ")
            print()
            if admin_choice1 == "1":
                try:
                    self.b.execute("SELECT COUNT(*) FROM bnk")
                    total_accounts = self.b.fetchone()[0]
                    print("-"*25)
                    print("Total Number of Accounts:", total_accounts)
                    print("-"*25)
                except mysql.connector.Error as err:
                    print("Error fetching data:", err)

            elif admin_choice1 == "2":
                try:
                    self.b.execute("SELECT age FROM bnk")
                    customer_ages = [row[0] for row in self.b.fetchall()]

                    if customer_ages:  
                        plt.figure(figsize=(8, 6))
                        plt.hist(customer_ages, bins=20, color='skyblue', edgecolor='black')
                        plt.xlabel('Age')
                        plt.ylabel('Number of Customers')
                        plt.title('Age Distribution of Bank Customers')
                        plt.grid(True)
                        plt.show()
                    else:
                        print("No data available to generate the graph.")

                except mysql.connector.Error as err:
                    print("Error fetching data:", err)

            elif admin_choice1 == "3":
                print("Exiting Generate Reports...")
                return
    # by admin
    def close_account(self):
        
       
            name_to_delete = input("\nEnter Name: ")
            confirm = input("\nAre you sure you want to delete your account? (yes/no): ").lower()

            if confirm == "yes":
                try:
        # Find the user's ID based on the provided name
                    select_user_query = "SELECT aadhar FROM bnk WHERE name = %s"
                    self.b.execute(select_user_query, (name_to_delete,))
                    user_id = self.b.fetchone()

                    if user_id:
                        user_id = user_id[0]  # Extract the user ID from the result

            # Check if there are related records in the transaction table
                        check_transaction_query = "SELECT * FROM transaction WHERE user_id = %s"
                        self.b.execute(check_transaction_query, (user_id,))
                        related_records = self.b.fetchall()

                        if related_records:
                # Delete related records in the transaction table first
                            delete_transaction_query = "DELETE FROM transaction WHERE user_id = %s"
                            self.b.execute(delete_transaction_query, (user_id,))
                            self.a.commit()  # Commit the transaction

            # Proceed with deleting the user's account from the bnk table
                        delete_bnk_query = "DELETE FROM bnk WHERE aadhar = %s"
                        self.b.execute(delete_bnk_query, (user_id,))
                        self.a.commit()  # Commit the transaction

                        print("\nAccount deleted successfully.")
                        self.home()
                    else:
                        print("\nUser not found.")
                    

                except Exception as e:
                    print("Error deleting account:", e)

            else:
                print("\nAccount deletion canceled.") 
    
    def home(self):
         print()
         print()
         print()
         print()
        #  print("\n----->|  Welcome to SBI  |<-----")
         print("*****************************************")
         print("*                                       *")
         print("*      Welcome to the SBI Bank!         *")
         print("*                                       *")
         print("*****************************************")


         while(True):
             print("....................")
             print("1. Create Account \n2. Login Account \n3. Admin \n4. Exit")
             print("....................")
             choice = (input("Enter your choice : "))
             if choice == "1":
                 print()
                 print(" >>>>>>>>>>>>>>>> Create Account <<<<<<<<<<<<<<< ")
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

             elif choice == "4":
                print("\nExiting the program. Goodbye!")
                exit()   
             else:
                 print("\nInvalid choice. Please try again.")

    def createdb(self):
        try:
            self.b.execute('''
                CREATE TABLE IF NOT EXISTS bnk(
                name VARCHAR(20) NOT NULL,
                age INT NOT NULL,
                phone INT NOT NULL,
                location VARCHAR(20) NOT NULL,
                aadhar BIGINT PRIMARY KEY,
                pan VARCHAR(10) UNIQUE,
                pin INT NOT NULL,
                balance DECIMAL(10, 2) DEFAULT 0.00
            )
        ''')
            self.b.execute('''
            CREATE TABLE IF NOT EXISTS transaction(
            transaction_id INT AUTO_INCREMENT PRIMARY KEY,
            user_id BIGINT NOT NULL,
            amount DECIMAL(10, 2) NOT NULL,
            transaction_type ENUM('Deposit', 'Withdrawal') NOT NULL,
            transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES bnk(aadhar)
        )
    ''')
            self.a.commit()
            print("table created")
        except mysql.connector.Error as err:
            print("Error creating tables:", err)
    
    def insertdb(self):
         
            check_aadhar_query = "SELECT COUNT(*) FROM bnk WHERE aadhar = %s"
            self.b.execute(check_aadhar_query, (self.aadhar,))
            result = self.b.fetchone()

            if result[0] > 0:
                print("Aadhar number already exists. Please enter a different Aadhar number.")
                
            else:
                insert_query = "INSERT INTO bnk(name, age, phone, location, aadhar, pan, pin) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = (self.name, self.age, self.phone, self.loc, self.aadhar, self.pan, self.Pin)
                self.b.execute(insert_query, values)
                self.a.commit()
                print("Record Inserted")

    

obj = Bank()
obj.createdb()
obj.home()
                                                  