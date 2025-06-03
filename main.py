from cs50 import SQL
import methods as m




# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///Data.db")

m.banner()
flag = True
while(True):
    flag = True

    count = 0
    data = db.execute("SELECT * FROM accounts")
    ids = []

    for x in data:
        print("\n[ id:",x["id"], " |balance:",x["endBalance"], " |description:",x["name"], "]")

        ids.append(x["id"])

    while(flag):

        while(flag):

            try:
                print("--------------------------------------")
                choose = int(input('\nChoose id: \"number\" from above\nAdd new account: 0\nExit: -1\nPrint ids: -2\nDelete account: -3\nPrint banner: -4\n--------------------------------------\nchoose: '))
                break

            except ValueError:
                print('\nEnter a valid integer or type new')

        if choose in ids:
            print("\n")
            #after choose id
            while(True):
                print("--------------------------------------")
                print("--------------------------------------")
                print("add money to this account: 1\nview added money: 2\nview all records in this account: 3\nmake new operation: 4\nprofit you make: 5\nprint account detail: 6\nPrint profit/losses: 7\ngo back: 8")
        
                print("--------------------------------------")
                print("--------------------------------------")
                choose2 = int(input('choose a number: '))

                if choose2 == 1:
                    m.addMoney(choose)

                if choose2 == 2:
                    m.addedMoney(choose)

                if choose2 == 3:
                    m.View(choose)

                if choose2 == 4:
                    m.Enter(choose)

                if choose2 == 5:
                    m.dif(choose)

                if choose2 == 6:
                    m.ViewAccount(choose)

                if choose2 == 7:
                    m.WL(choose)

                if choose2 == 8:
                    break



            break
        #add new account
        if choose == 0:
            m.NewAccount()
            flag = False
            break

        if choose == -1:
            m.Ex()
        if choose == -2:
            print("\n")
            flag = False
            break

        if choose == -3:
            while(True):

                try:
                    choose3 = int(input('\nchoose id to delete or 0 to go back: '))
                    break

                except ValueError:
                    print('\\nchoose id \"integer\" to delete or 0 to go back:')

            if choose3 in ids:
                print("\n")
                m.dele(choose3)
                flag = False
                break

            if choose3 == 0:
                flag = False
                break

        if choose == -4:
            m.banner()
            break




        print("\nyou should choose from", ids, ", type 0 for new account\nExit -1 , Print ids -2\nDelete account -3 , Print banner -4")
