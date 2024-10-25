def SPLASH_SCREEN(username):
    return f'''\033[91m
     _                                          
    | |                                         
 ___| |_ _ __ __ ___      ___ \033[93m__   __ _ ___ ___ 
\033[91m/ __| __| '__/ _` \ \ /\ / / \033[93m'_ \ / _` / __/ __|
\033[91m\__ \ |_| | | (_| |\ V  V /\033[93m| |_) | (_| \__ \__ \\
\033[91m|___/\__|_|  \__,_| \_/\_/ \033[93m| .__/ \__,_|___/___/
     the password manager  | |    {username}            
                           |_|                  
    \033[0m'''

class PasswordManager:
    def __init__(self, username, password_file):
        self.username = username
        self.password_file = password_file

    def __str__(self):
        return SPLASH_SCREEN(self.username)
    
    def help_cmd(self):
        def addline(cmd, msg):
            print("\033[93m\t" + cmd + "\033[0m - " + msg)

        print("\033[91m" + "Commands" + "\033[0m")

        addline("help", "displays this screen")
        addline("log [user] [pwd]", "adds a username/password entry")
        addline("fetch [user]", "fetches the password for the given user")
        addline("view", "view all usernames for which a password exists")
        addline("exit", "exits this program")

    def addPassword(self, username, password):
        with open(self.password_file, 'a') as file:
            file.write(f"{username}:{password}\n")

    def fetchPassword(self, username):
        with open(self.password_file, 'r') as file:
            for line in file:
                stored_username, stored_password = line.strip().split(':')
                if stored_username == username:
                    print(stored_password)
                    return
        print("Password not found")
    
    def viewAll(self):
        with open(self.password_file, 'r') as file:
            for line in file:
                stored_username, _ = line.strip().split(':')
                print(stored_username)

def main():
    username = input("select a username: ")
    password_file = input("select a password file: ")

    PM = PasswordManager(username, password_file)
    print(PM)

    PM.help_cmd()

    while True:
        args = input("$ ").strip().split(" ")
        cmd = args[0]

        if cmd == "help":
            PM.help_cmd()
            continue

        if cmd == "log":
            user = args[1]
            pwd = args[2]
            PM.addPassword(user, pwd)
            continue

        if cmd == "fetch":
            user = args[1]
            PM.fetchPassword(user)
            continue

        if cmd == "view":
            PM.viewAll()
            continue

        if cmd == "exit":
            return 0

        print("Command not known.")
        continue

main()