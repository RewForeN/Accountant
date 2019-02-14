
import os
import re

os.system('clear')


class BankAccount:

    def __init__(self, index=0, name="MyAccount", balance=0.00, history=[]):
        self.index = index
        self.name = name
        self.balance = round(balance, 2)
        self.history = history

    def __str__(self):
        # Return this account's details
        returnString = """--- Account Details ---\n
            Name: %s
            Balance: $%s
            """ % (self.name, self.balance)
        return returnString

    def addFunds(self, amount):
        # Add funds to this account
        self.balance += amount
        self.history.append(self.balance)
        self.saveAccount()

    def changeName(self, newName):
        # Change name of this account
        self.name = newName
        self.saveAccount()

    def saveAccount(self):
        # Save this account's details
        with open(path + "acc%s" % self.index, 'w') as f:
            f.write("<name>%s</name>\n" % self.name)
            f.write("<balance>%s</balance>\n" % self.balance)
            f.write("<history>\n")
            for i in self.history:
                f.write("%s\n" % i)
            f.write("</history>")

    def showHistory(self):
        # Show this account's history
        print()
        for ch in self.history:
            print(ch + ",  ", end="")
        print("\n")
        input("Press enter to continue...")


# Global #
path = "bin/"
accounts = []


def getAll():
    # Return names of all existing accounts
    return accounts


def new():
    # Create a new Bank Account
    name = input("New account name: ")
    balance = input("New account starting balance: ")
    balance = round(float(balance), 2)
    account = BankAccount(len(accounts), name, balance, [balance])
    account.saveAccount()
    accounts.append(account)


def showAccountDetails(account):
    # Show account details
    print(account)


def delete(account):
    # Delete account
    print("Deleting account", account.name)


# Get all files in path
try:
    files = os.listdir(path)
except FileNotFoundError:
    os.mkdir(path)
    files = os.listdir(path)

if (len(files) == 0):
    # Create first account
    print("No accounts currently exist")
    print("You must create a new account to continue\n")
    new()
else:
    # Add all existing accounts to accounts list
    files = os.listdir(path)
    for i in range(len(files)):
        with open(path + files[i]) as f:
            lines = f.read()
            name = re.findall("<name>(.*?)</name>", lines)
            balance = re.findall("<balance>(.*?)</balance>", lines)
            historyString = re.findall("(?s)<history>(.*?)</history>", lines)
            history = re.findall("[\n](.+)", historyString[0])
            accounts.append(BankAccount(
                i, name[0], float(balance[0]), history))
