user = {
    "dipanshu" : "9110",
    "rohan" : "4324",
    "rajaryan": "9608",
    "aryan": "9934",
    "rohit": "2345",
    "mukesh": "6523"
}
def loginsystem():
    username = input("enter username: ").lower()
    password = input("enter password: ")

    if username in user:
        if user[username] == password:
            print("LOGIN SUCCESSFULLY\nTHANK YOU")
        elif user[username] != password:
            print("ENTERED WRONG PASSWORD,\n Try Again")

loginsystem()