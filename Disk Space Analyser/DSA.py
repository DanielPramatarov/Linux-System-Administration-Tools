# # from github import Github

# # # First create a Github instance:

# # # using username and password
# # g = Github("danielpramatarov", "Borecadaniellotta15052001")
# # user =g.get_user()
# # user.login
# # for repo in user.get_repos():
# #     print(repo.name)


# import webbrowser

# webbrowser.open("www.abv.bg")


# import getpass
# user  = getpass.getuser()
# password  = getpass.getpass()

# if 1 == 1:
#     print(user)
# else:
#     print("NOOO")

# import crypt, getpass, spwd
# def check_pass():
#    username = input("Enter The Username: ")
#    password = spwd.getspnam(username).sp_pwdp
#    if password:
#       clr_text = getpass.getpass()
#       return crypt.crypt(clr_text, password) == password
#    else:
#       return 1
        
# if check_pass():
#    print("The password matched")
# else:    
#    print("The password does not match")




import subprocess
from colorama import Fore, Back, Style 

def banner():
    ban = f"""{Fore.LIGHTCYAN_EX}
██████╗ ███████╗ █████╗ 
██╔══██╗██╔════╝██╔══██╗
██║  ██║███████╗███████║
██║  ██║╚════██║██╔══██║
██████╔╝███████║██║  ██║
╚═════╝ ╚══════╝╚═╝  ╚═╝
                         
  {Style.RESET_ALL}
  {Fore.CYAN}DISK SPACE ANALYSER\n       FOR LINUX{Style.RESET_ALL}                               
 """
    print(ban)




banner()

child = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE)
output = (child.communicate()[0].strip().decode("UTF-8").split("\n"))
for x in output[1:]:
      args = x.split()
      name = args[0]
      full_space = args[1]
      used_space = args[2]
      free_space = args[3]
      percent_used_space = args[4]
      path_to_the_disk = args[5]
      intPercentage = percent_used_space.split("%")
      delimiterOutput = "="*100
      if int(intPercentage[0]) <= 50:
            print(f"{delimiterOutput}\n")
            print(f"Disk name ->{Fore.GREEN} {name}\n{Style.RESET_ALL}Percentage used capacity -> {Fore.GREEN}{percent_used_space}  {Style.RESET_ALL}\nFree space -> {Fore.GREEN}{free_space}{Style.RESET_ALL}\nMaximal capacity -> {Fore.GREEN}{full_space}{Style.RESET_ALL}\nUsed space {Fore.GREEN}{used_space}{Style.RESET_ALL}\nLocation to the disk -> {Fore.GREEN}{path_to_the_disk}{Style.RESET_ALL}\n")
      elif int(intPercentage[0]) > 50 and int(intPercentage[0]) <= 75:
            print(f"{delimiterOutput}\n")
            print(f"{Fore.LIGHTYELLOW_EX}WARNING !!!{Style.RESET_ALL}\n")
            print(f"Disk name ->{Fore.LIGHTYELLOW_EX} {name}\n{Style.RESET_ALL}Percentage used capacity -> {Fore.LIGHTYELLOW_EX}{percent_used_space}  {Style.RESET_ALL}\nFree space -> {Fore.LIGHTYELLOW_EX}{free_space}{Style.RESET_ALL}\nMaximal capacity -> {Fore.LIGHTYELLOW_EX}{full_space}{Style.RESET_ALL}\nUsed space {Fore.LIGHTYELLOW_EX}{used_space}{Style.RESET_ALL}\nLocation to the disk -> {Fore.LIGHTYELLOW_EX}{path_to_the_disk}{Style.RESET_ALL}\n")
            
      elif int(intPercentage[0]) > 75 and int(intPercentage[0]) <= 100:
            print(f"{delimiterOutput}\n")
            print(f"{Fore.RED}IMPORTANT !!! RUNNING OUT OF DISK SPACE {Style.RESET_ALL}\n")
            print(f"Disk name ->{Fore.RED} {name}\n{Style.RESET_ALL}Percentage used capacity -> {Fore.RED}{percent_used_space}  {Style.RESET_ALL}\nFree space -> {Fore.RED}{free_space}{Style.RESET_ALL}\nMaximal capacity -> {Fore.RED}{full_space}{Style.RESET_ALL}\nUsed space {Fore.RED}{used_space}{Style.RESET_ALL}\nLocation to the disk -> {Fore.RED}{path_to_the_disk}{Style.RESET_ALL}\n")
print(delimiterOutput)