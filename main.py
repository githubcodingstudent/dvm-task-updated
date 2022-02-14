import csv
import os


class ATM:
    def __init__(self):
        # checks if database.csv exists
        if os.path.isfile('./database.csv') == False:
            # creates database.csv
            open('database.csv', 'x')

    # prompts the new user for input for registration
    def register(self):
        while True:
            ac = input('Account number:')
            with open('database.csv', 'r', newline='') as db:
                rd = csv.reader(db)
                existing = []
                while True:
                    try:
                        existing.append(next(rd)[0])
                    except StopIteration:
                        break
                #checks for existing accounts
                if ac in existing:
                    print('Account already exists. Try again')
                else:
                    break
        #prompts user to set a pin
        while True:
            pin = input('Pin(4-digit): ')
            if not len(pin) == 4:
                print('Pin length incorrect')
            elif not pin.isnumeric():
                print('Please enter a numeric PIN.')
            elif pin == input('Verify Pin: '):
                break
            else:
                print('Pins do not Match enter again.')
        #adds new account information to the database
        with open('database.csv', 'a', newline='') as db:
            db_wtr = csv.writer(db)
            db_wtr.writerow([ac, pin, 0])
            db.close()

        print('Successfully registered')
#prompts existing user to login
    def access(self):
        ac = input("Enter your account number: ")
        pin = input("Enter your pin: ")
        with open('database.csv', 'r', newline='') as db:
            rd = csv.reader(db)
            for i in rd:
                if i[0] == ac:
                    if i[1] == pin:
                        balance = int(i[2])
                    else:
                        print('Incorrect PIN')
                        return
                    break
            else:
                print('Account not found.')
                return
#prompts user to choose a money transaction from the menu
        choice = 0
        while choice != 4:
            print("\n\n**** Menu *****")
            print("1 == balance")
            print("2 == deposit")
            print("3 == withdraw")
            print("4 == cancel\n")

            choice = int(input("\nEnter your option:\n"))
            if choice == 1:
                print("Balance = ", balance)
            elif choice == 2:
                dep = int(input("Enter your deposit: "))
                balance += dep
                print("Deposited amount: ", dep)
                print("Balance = ", balance)
            elif choice == 3:
                wit = int(input("Enter the amount to withdraw: "))
                if balance < wit:
                    print("Insufficient Balance.")
                    continue
                balance -= wit
                print("Withdrawn amount: ", wit)
                print("Balance = ", balance)
            elif choice == 4:
                #updates the database
                  #creates temporary file for the duration of the transaction
                  #replaces database with temporary file
                  #renames the temporary file
                with open('database.csv', 'r', newline='') as db, open('temp.csv', 'w', newline='') as new:
                    rd = csv.reader(db)
                    wt = csv.writer(new)
                    for i in rd:
                        if i[0] == ac:
                            i[2] = str(balance)
                        wt.writerow(i)
                    db.close()
                    new.close()
                os.remove('database.csv')
                os.rename('temp.csv', 'database.csv')
                print('Session ended,goodbye.')
            else:
                print("Invalid Entry")
#prompts the user to choose Login or Signup
    def home(self):
        option = input("Login | Signup: ")
        if option.lower() == "login":
            self.access()
        elif option.lower() == "signup":
            self.register()
        else:
            print("Please choose an option")


# creating bank object
bank = ATM()

if __name__ == '__main__':
    while True:
        bank.home()