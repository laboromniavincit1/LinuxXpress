import os
import getpass  # getpass has a fucntion to input string without echo back to screen (for taking input password )
# to change the color of terminal 
os.system("tput setaf 2")
print("\t\t\tHey Welcome to My TUI that makes life easier : ")
# to change the color of terminal
os.system("tput setaf 7")
print("\t\t\t----------------------------------------------")

tryy = 0
while (tryy <= 2):
    passwd = getpass.getpass("Enter your password : ")
    password = '1234'
    if passwd == password:
        location=input("Where you want to execute commands (local/remote): ")
        if location == 'local':
            while(True): 
                print("""
                Press 1 : check cal  
                Press 2 : See date  
                Press 3 : Make directory 
                Press 4 : Create File 
                Press 5 : Create a User 
                Press 6 : Delete a User
                Press 7 : Change Password of a User
                Press 8 : Configure Web Server
                Press 9 : DockEase
                Press 10: Exit 
                """)
                choice = input("Enter your choice : ")
                if choice == '1':
                    print(os.system("cal"))
                elif choice == '2':
                    print(os.system("date"))
                elif choice == '3':
                    dir = input("Enter the name of directory : ")
                    os.system("mkdir {}".format(dir))
                elif choice == '4':
                    file = input("Enter name of File : ")
                    os.system("touch {}".format(file))
                elif choice == '5':
                    username = input("Enter the name of user : ")
                    os.system("sudo useradd {}".format(username))
                    os.system("sudo passwd {}".format(username))
                elif choice == '6':
                    userdel = input("Enter the name of user : ")
                    os.system("sudo userdel {}".format(userdel))
                elif choice == '7':
                    userpasswd = input("Enter the name of user: ")
                    os.system("sudo passwd {}".format(userpasswd))
                elif choice == '8':
                    os.system("sudo dnf install httpd")
                    os.system("sudo systemctl start httpd")
                elif choice == '9':
                    os.system("node server.js")
                elif choice == '10':
                    exit()
                else:
                    print("Not a valid Option !!")
                input("Enter to Continue")
                os.system("clear")
        elif location == 'remote':
            remoteIP = input("Enter the IP : ")
            os.system("ssh-keygen")
            os.system("ssh-copy-id root@{}".format(remoteIP))
            while(True): 
                print("""
                Press 1 : check cal  
                Press 2 : See date  
                Press 3 : Make directory 
                Press 4 : Create File 
                Press 5 : Create a User 
                Press 6 : Delete a User
                Press 7 : Change Password of a User
                Press 8 : Configure Web Server
                Press 9 : DockEase
                Press 10: Exit 
                """)
                choice = input("Enter your choice : ")
                if choice == '1':
                    print(os.system("ssh root@{} cal".format(remoteIP)))
                elif choice == '2':
                    print(os.system("ssh root@{} date".format(remoteIP)))
                elif choice == '3':
                    dir = input("Enter the name of directory : ")
                    os.system("ssh root@{0} mkdir {1}".format(remoteIP, dir))
                elif choice == '4':
                    file = input("Enter name of File : ")
                    os.system("ssh root@{} touch {}".format(remoteIP, file))
                elif choice == '5':
                    username = input("Enter the name of user : ")
                    os.system("ssh root@{} sudo useradd {}".format(remoteIP,username))
                    os.system("ssh root@{} sudo passwd {}".format(remoteIP,username))
                elif choice == '6':
                    userdel = input("Enter the name of user : ")
                    os.system("ssh root@{} sudo userdel {}".format(remoteIP, userdel))
                elif choice == '7':
                    userpasswd = input("Enter the name of user: ")
                    os.system("ssh root@{} sudo passwd {}".format(remoteIP, userpasswd))
                elif choice == '8':
                    os.system("ssh root@{} sudo dnf install httpd".format(remoteIP))
                    os.system("ssh root@{} sudo systemctl start httpd".format(remoteIP))
                elif choice == '9':
                    os.system("ssh root@{} ifconfig".format(remoteIP))
                elif choice == '10':
                    exit()
                else:
                    print("Not a valid Option !!")
                input("Enter to Continue")
                os.system("clear")
        else:
            print("Not a valid Option !!")
    else:
        print("Auth Failed!! Try again")
        tryy +=1
