import os 
import subprocess 
import sys 
import getpass 
from colorama import Fore, Back, Style 
from subprocess import Popen, PIPE
import pwd, grp
import time

def banner():
    ban = f"""{Fore.LIGHTCYAN_EX}
██╗   ██╗ ██████╗ ███╗   ███╗████████╗
██║   ██║██╔════╝ ████╗ ████║╚══██╔══╝
██║   ██║██║  ███╗██╔████╔██║   ██║   
██║   ██║██║   ██║██║╚██╔╝██║   ██║   
╚██████╔╝╚██████╔╝██║ ╚═╝ ██║   ██║   
 ╚═════╝  ╚═════╝ ╚═╝     ╚═╝   ╚═╝   
  {Style.RESET_ALL}
  {Fore.CYAN}USER & GROUP MANAGEMENT TOOL\n\t  FOR LINUX{Style.RESET_ALL}                               
 """
    print(ban)

def cheack_existing_user(user):

    linux_users = []
    for p in pwd.getpwall():
        linux_users.append(p.pw_name)
    if user in linux_users:
        return True
    else:
        return False

def add_user(username, password): 
 
    try: 
        subprocess.run(['useradd', '-p', password, username ])   
        print(f"Successfully added user => {Fore.GREEN}{username}{Style.RESET_ALL}")    
    except: 
        print(f"Failed to add user {Fore.GREEN}{username}{Style.RESET_ALL}")                      
        sys.exit(1) 

def delete_user(username): 
    print(f"{Fore.RED}==================== Deleting User !!! ===================={Style.RESET_ALL}")
    if cheack_existing_user(username):

        try: 
            output = subprocess.run(['userdel', username ]) 
            if output.returncode == 0: 
                print(f"User {Fore.GREEN}{username}{Style.RESET_ALL} has been deleted successfully") 

        except: 
            print(f"Failed to delete user {Fore.GREEN}{username}{Style.RESET_ALL}") 
            sys.exit(1) 
 
    else:
         print(f"Username {username} does not exist")
         

def change_pass(username, password):
    if cheack_existing_user(username):
        try:
            proc=Popen(['passwd', username],stdin=PIPE,stdout=PIPE,stderr=PIPE)
            proc.stdin.write(password + b'\n')
            proc.stdin.write(password)
            proc.stdin.flush()
            stdout,stderr = proc.communicate()
            time.sleep(0.1)
            print(stderr.decode("UTF-8").split(': ')[3].strip())
        except Exception as ex:
            print(str(ex))
    else:
        print(f"Username {username} does not exist")

banner()

if not os.geteuid()==0:
    sys.exit(f"{Fore.LIGHTRED_EX}This script must be run as root!{Style.RESET_ALL}")
print("0 - EXIT")
print("1 - Create new user")
print("2 - Delete user")
print("3 - Change password of specific user")

ch = int(input(f"{Fore.YELLOW}Your choice =>{Style.RESET_ALL} "))

while True:

    if ch == 0:
        sys.exit(1)


    elif ch == 1:
        username = input("Enter Username ")    
        password = getpass.getpass() 
        add_user(username, password)
    elif ch == 2:
        username = input("Enter Username : ")
        choice = str(input(f"Are you sure you want to delete this User => {Fore.RED}{username}{Style.RESET_ALL} ? [yes] or [no] : "))
        if choice.lower() == "yes":
            delete_user(username)
        else:
            pass

    elif ch == 3:
        username = input("Enter Username : ")
        password = input("Enter New Password : ")
        password = str.encode(password)

        change_pass(username,password)
    ch = int(input(f"{Fore.YELLOW}Your choice =>{Style.RESET_ALL} "))
    


