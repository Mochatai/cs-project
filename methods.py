import sys
from cs50 import SQL
import datetime



# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///Data.db")

#Delete all data related
def dele(val):

    db.execute("DELETE FROM records where user_id=%s" % (val))
    db.execute("DELETE FROM accounts where id=%s" % (val))
    db.execute("DELETE FROM added where user_id=%s" % (val))



#calculate profit percentage
def dif(val):
    #get account data
    data = db.execute("SELECT * FROM accounts WHERE id =%s" % (val))

    #get balance and endbalance
    start = data[0]["balance"]
    end = data[0]["endBalance"]

    #calculate profit
    if start > end:
        eq = (end - start) / start *100

    if start < end:
        eq = (end - start) / start *100

    if start == end:
        eq = 0

    #make it .00
    eq = round(eq, 2)

    #print profit
    print("your account profit is ",eq,"%")

#exit
def Ex():
    sys.exit()

#make new operation
def Enter(val):

    #get user data
    data = db.execute("SELECT * FROM accounts WHERE id =%s" % (val))

    #endBalance
    user_input = data[0]["endBalance"]

    #print starting point
    print("The amount you start with is:",user_input )
    while(True):
        try:
            #get user input
            user_output = float(input('The amount you end with after: '))
            break

        except ValueError:
            print('Enter a valid float')

    #determine the resulting
    if user_output > user_input:
        WL = "Win"

    if user_output < user_input:
        WL = "Lose"

    if user_output == user_input:
        WL = "Draw"

    #Calculate profit
    profit = user_output - user_input
    #get system time
    time = datetime.datetime.now()

    #insert data into records
    db.execute("INSERT INTO records (user_id, start, end, profit, time, WL) VALues(?, ?, ?, ?, ?, ?)",val, user_input,  user_output, profit, time, WL)
    #update account
    db.execute("UPDATE accounts SET endBalance =%s WHERE id = %s",user_output, val)

#view records
def View(val):
    #get records from database
    data = db.execute("SELECT * FROM records WHERE user_id =%s" % (val))
    count = 1

    #format
    for x in data:
        print("-------------------------------")
        print("|you enter with: $", x["start"])
        print("|you exit with: $", x["end"])
        print("|your profit is: $", x["profit"])
        print("|time : ", x["time"])
        print("-------------------------------")
        count = count + 1

#add new account
def NewAccount():

    while(True):
        try:
            #user account balance
            balance = float(input('The balance of your account: '))
            break

        except ValueError:
            print('Enter a valid float')

    while(True):
        try:
            #user account description
            text = input('account description: ')
            break

        except ValueError:
            print('Enter a valid float')

    #create an account
    db.execute("INSERT INTO accounts (balance, endBalance, name) VALues(?, ?, ?)", balance,  balance, text)
#view account details
def ViewAccount(val):
    #user data
    data = db.execute("SELECT * FROM accounts WHERE id=%s" % (val))

    #data format
    for x in data:
        print("\n|you start with: $",x["balance"])
        print("|you end up with: $",x["endBalance"])
        print("|account description : ", x["name"],"\n")


def addMoney(val):

    while(True):
        try:
            #get user input
            money = float(input('The amount you want to add: '))
            break

        except ValueError:
            print('Enter a valid float')

    #get user data
    data = db.execute("SELECT * FROM accounts WHERE id =%s" % (val))

    #get user balance
    user_input = data[0]["endBalance"]

    #add added money
    user_input = user_input + money

    #get system time
    time = datetime.datetime.now()

    #update account
    db.execute("UPDATE accounts SET endBalance =%s WHERE id = %s",user_input, val)

    #insert into added table
    db.execute("INSERT INTO added (user_id, amount, time) VALues(?, ?, ?)", val,  money, time)

def addedMoney(val):

    #get added history
    data = db.execute("SELECT amount, time FROM added WHERE user_id =%s" % (val))

    #print history
    for x in data:
        print("\n", "$", x["amount"],"added at",x["time"],"\n")

def banner():
    print('''
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████─██████─────────██████████████────██████████████─██████████████─██████████─██████──────────██████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░██─██░░██████████──██░░██─
─██░░██████████─██░░██████░░██─██░░██─────────██░░██████████────██░░██████████─██░░██████░░██─████░░████─██░░░░░░░░░░██──██░░██─
─██░░██─────────██░░██──██░░██─██░░██─────────██░░██────────────██░░██─────────██░░██──██░░██───██░░██───██░░██████░░██──██░░██─
─██░░██─────────██░░██████░░██─██░░██─────────██░░██────────────██░░██─────────██░░██████░░██───██░░██───██░░██──██░░██──██░░██─
─██░░██─────────██░░░░░░░░░░██─██░░██─────────██░░██────────────██░░██──██████─██░░░░░░░░░░██───██░░██───██░░██──██░░██──██░░██─
─██░░██─────────██░░██████░░██─██░░██─────────██░░██────────────██░░██──██░░██─██░░██████░░██───██░░██───██░░██──██░░██──██░░██─
─██░░██─────────██░░██──██░░██─██░░██─────────██░░██────────────██░░██──██░░██─██░░██──██░░██───██░░██───██░░██──██░░██████░░██─
─██░░██████████─██░░██──██░░██─██░░██████████─██░░██████████────██░░██████░░██─██░░██──██░░██─████░░████─██░░██──██░░░░░░░░░░██─
─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██────██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░██─██░░██──██████████░░██─
─██████████████─██████──██████─██████████████─██████████████────██████████████─██████──██████─██████████─██████──────────██████─
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
''')


def WL(val):

    #get data
    wData = db.execute("SELECT start, end, profit, time FROM records WHERE WL = \"Win\" And user_id = %s", (val))
    lData = db.execute("SELECT start, end, profit, time FROM records WHERE WL = \"Lose\" And user_id = %s", (val))
    wSum = db.execute("SELECT profit, SUM(profit) as sum FROM records WHERE WL = \"Win\" And user_id = %s", (val))
    lSum = db.execute("SELECT profit, SUM(profit) as sum FROM records WHERE WL = \"Lose\" And user_id = %s", (val))

    #earnings format
    print("earnings")
    print("--------------------------------------")
    for x in wData:
        print("Start: $", x["start"], "End: $", x["end"], "profit $", x["profit"], "Time:", x["time"])

    print("Sum of all earnings $", wSum[0]["sum"])

    print("--------------------------------------")
    #loses format
    print("losses")
    print("--------------------------------------")
    for x in lData:
        print("Start: $", x["start"], "End: $", x["end"], "profit $", x["profit"], "Time:", x["time"])
    print("Sum of all loses $", lSum[0]["sum"])

    print("--------------------------------------")



