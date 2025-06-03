# Calc gain

#### Description:
This program will help you with calculating gains and losses for daily trading. I noticed it was hard for me to record trading data so I made a program
that will save and present data in a specific format and help with some simple information presentation about your account like profit percentage.
For example, at the start of this program, you will encounter three options you can choose id (integer only) from accounts that already exist or
Add a new account by giving it a starting value and a description for its purpose the starting value will be the base for any calculation in this app.
Deleting an account will require an account ID and by deleting an account by entering the ID number of that account the app will delete any related data in the database.
Exit will terminate the program. After choosing any ID from the accounts you will encounter eight options. You can add money so you should enter an integer number your added
money will be appended with the starting value of your account. View added money: Any added money will be recorded in a table and printed in the terminal with the time of
added money. Make a new operation: You will be able to see how much you have so you need to enter the value you end with after the trade (the end value will be the new account balance).
View all records will print all operations you did as start (the account balance), exit(the amount you end with it the end), profit (for every operation the profit will be calculated from account balance and exit amount),
and time (the time of the operation). Profit you make will print profit/lose percentage (the equation will be calculated based on the account)
balance and account starting value). Account detail will print the starting value of the account (the value you entered when you created an account), end balance, and account description. Print profit/losses will print profit/loss for each
profitable operation and the total sum of profit and the same will be done to losses. Go back you can use this option to go back to the previous tab where you started at the beginning. I coded this app in Python and chose to make it command-based so it stays simple

This app is divided into three files.

main.py: All format and loops is in this file also error handling for every input.

methods.py: All methods used in this is in this file most of the methods take id as an argument.

Data.db: This database will sort all data needed for the program Most of the methods make quarries to this database.

The database is divided into three tables accounts, added and records. no relationship in this database but the relationship is forced by the program

accounts table will store account details such as ID, start value, end value, and description.
added table will store added money information like amount and time with the ID of the account.
records table will store information about any account that makes an operation.
