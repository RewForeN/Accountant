
from time import sleep
from os import system
import accountant


def main():

    while True:

        system('clear')

        print("Choose an action:")
        print("N = New account")
        print("Q = Quit")
        print("\nor\n")
        print("Select an account:")

        accounts = accountant.getAll()
        for acc in accounts:
            print(str(acc.index) + ": " + acc.name)

        prompt = input("\n>> ")
        print()

        if (prompt.lower() == "n"):
            accountant.new()
            continue
        elif (prompt.lower() == "q"):
            return

        try:
            index = int(prompt)
            selectAccount(accounts[index])
        except:
            print("Invalid action")
            sleep(1)
            raise Exception
            continue


def selectAccount(account):

    system('clear')
    sleep(0.1)
    accountant.showAccountDetails(account)

    print("Choose an action: ")
    print("B = Go back")
    print("1 = Add funds")
    print("2 = Withdraw money")
    print("3 = Show history")
    print("4 = Change account name")
    print("5 = Delete account")

    prompt = input("\n>> ")

    if (prompt.lower() == "b"):
        return
    elif (prompt.lower() == "1"):
        amount = float(input("Amount: "))
        account.addFunds(amount)
    elif (prompt.lower() == "2"):
        amount = float(input("Amount: "))
        account.addFunds(-amount)
    elif (prompt.lower() == "3"):
        account.showHistory()
    elif (prompt.lower() == "4"):
        newName = input("New name: ")
        account.changeName(newName)
    elif (prompt.lower() == "5"):
        accountant.delete(account)
    else:
        print("Invalid action")
        selectAccount(account)
    selectAccount(account)


if __name__ == "__main__":
    main()
