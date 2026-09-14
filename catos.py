import datetime
import time
import random

# print("Creating Files...")
# time.sleep(0.5)
# print("Loading: testfile")
# time.sleep(random.uniform(0.1, 0.2))
# print("Loading: usr.conf")
# time.sleep(random.uniform(0.1, 0.2))
# print("Loading: users.conf")
# time.sleep(1)
# print("Loading: passwords.conf")
# time.sleep(1)
# print("Creating CathM")
# print("Getting stdio.catc")


bcioslog = []

files = {
    "testfile" : {
        "content" : "AGRRRRRRRRRRRRRRRRRRRRRRRRRRR dinosavr"
    },
    "usr.conf" : {
        "content" : r"Cat@root0 \0"
    },
    "users.conf" : {
        "content" : {
            "Cat" : "root",
            "Administrator" : "root0",
            "guest" : "guest"

        }
    },
    "passwords.conf" : {
        "content" : {
            "Cat" : "123",
            "Administrator" : "password"
        }
    },
    "stdio.catc" : {
        "content" : "library for future CathM"
    }
}
bcioslog.append("Booted CatOS files. \n")

sysfilenames = ["usr.conf", "users.conf", "passwords.conf", "stdio.catc"]

# class File:
#     def __init__(self, name, content):
#         self.name = name
#         self.content = content

recovery = False

print(
    r"""
  ____      _        ____        __ _   
 / ___|__ _| |_ ___ / ___|  ___ / _| |_
| |   / _` | __/ _ \\___ \ / _ \ |_| __|
| |__| (_| | || (_) |___) |  __/  _| |_
 \____\__,_|\__\___/|____/ \___|_|  \__|
"""
)
print("CatoSoft CatOS [Version 0.1 Indev]")
print("(c) CatoSoft Corporation. All rights reserved.")
bcioslog.append("User: ", files.get("usr.conf")["content"])
ignore = False

while True:
    while not recovery:
        bcioslog.append("Syscall [Return] \n")
        try:
            rawuser = files.get("usr.conf")["content"]
            # Strip \0 and extra whitespace so user['name'] is cleanly "root0", "user", or "guest"
            clean_user = rawuser.replace(r"\0", "").strip()
            user = {
                "privilege": clean_user.split("@")[0].strip(),
                "name": clean_user.split("@")[1].strip()
            }
        except (TypeError, IndexError):
            time.sleep(0.1)
            print("):")
            print("Your PC ran into a problem we cant solve (we also wont)")
            print("CatOS has run into a critical error.")
            print("\n")
            time.sleep(0.1)
            print("ERR_CODE: womp womp")
            print("Check your BCIOS log for error details.")
            bcioslog.append("SysCrashed")
            print("\n\n\n")
            recovery = True
            break
        inp = str(input(f"/Users/{user['privilege']}~$ "))

        if inp.startswith("sudo"):
            bcioslog.append("Syscal [sudo] \n")
            if user["name"] == "root0":
                print("You are already root.")
            else:
                password = input("Enter the root password: ")
                if password == files.get("passwords.conf")["content"].get("Administrator"):
                    print("Successfully elevated to root.")
                    ignore = True
                    inp = inp[5:].strip()
                    continue
                else:
                    print("[CatError -006] Incorrect password.")
                    continue

        if inp == "help":
            print("crt filename.txt  -  create a text file")
            print("rm filename.txt  -  remove a file")
            print("set filename.txt  -  execute a script file")
            print("cat filename.txt  -  read the target file")
            print("wr filename.txt  -  edit a files contents")
            print("user  -  prints the active user.")
            print("user -priv  -  prints the active user and their privilege level.")
            print("list  -  lists all files and directories in the active directory")
            print("logout  -  logs out of the current user account")
            print("login username  -  logs in as the specified user")
            print("cls  -  clears the screen")
            print("")
            print("NOTE: guest account cant perform any actions except logging in.")

        elif inp.startswith("crt"):
            if files.get("usr.conf")["content"] != r"guest@guest \0" or ignore == True:
                newfilename = inp[4:].strip()
                if newfilename == "":
                    print("[CatError 004] The file name cannot be blank.")
                elif newfilename in files:
                    print("[CatError 001] The target file already exists.")
                else:
                    files[newfilename] = { "content" : "" }
            else: print("[CatError 003] You do not have permission to create files.")

        elif inp.startswith("cat"):
            if files.get("usr.conf")["content"] != r"guest@guest \0" or ignore == True:
                targetfile = inp[4:].strip()
                try:
                    content = files[targetfile]["content"]
                    if isinstance(content, dict):
                        for key, val in content.items():
                            print(f"{key}: {val}")
                    else:
                        print(content.removesuffix(r"\0") if content.endswith(r"\0") else content)
                except (NameError, KeyError):
                    # throw.error()
                    print(f"[CatError 002] There is no file named {targetfile} in the current directory.")
            else: print(f"[CatError 003] You do not have permission to read files.")

        elif inp == "ls" or inp == "list":
            print("Files in current directory:")
            for file in files:
                print(file)

        elif inp.startswith("rm"):
            if files.get("usr.conf")["content"] != r"guest@guest \0" or ignore == True:
                targetfile = inp[3:].strip()
                bcioslog.append(f"Syscall [rm {targetfile}]")
                if targetfile in sysfilenames and (user["name"] != r"root0" and ignore == False):
                    print(f"[CatError 003] You do not have permission to remove {targetfile}.")
                    continue
                try:
                    files.pop(targetfile)
                except (NameError, KeyError, TypeError):
                    print(f"[CatError 002] There is no file named {targetfile} in the current directory.")
            else: print("[CatError 003] You do not have permission to remove files.")

        elif inp.startswith("wr"):
            if files.get("usr.conf")["content"] != r"guest@guest \0" or ignore == True:
                targetfile = inp[3:].strip()
                if targetfile in sysfilenames and (user["name"] != r"root0" and ignore == False):
                    print(f"[CatError 003] You do not have permission to edit {targetfile} [0].")
                    bcioslog.append(f"Syscall [wr {targetfile}] - Acces Denied")
                    continue
                try:
                    thefile = files.get(targetfile)["content"]
                    if targetfile in sysfilenames and files.get("usr.conf")["content"].split("@")[1] != r"root0 \0" and ignore == False:
                        print(f"[CatError 003] You do not have permission to edit {targetfile}.")
                    else:
                        thefile = files.get(targetfile)["content"]
                        print(fr"Editing {targetfile}, type the new content, at the end of the document, make a new line and enter '\0'")
                        lines = []
                        while True:
                            line = input()
                            if line.strip() == r"\0":
                                break
                            if line.endswith(r"\0"):
                                lines.append(line)
                                break
                            lines.append(line)

                            bcioslog.append(fr"Syscall [wr {targetfile}] - {targetfile} content changed to '{"\n".join(lines)}'.")
                        
                        files[targetfile]["content"] = "\n".join(lines)
                except (NameError, KeyError, TypeError):
                    print(f"[CatError 002] There is no file named {targetfile} in the current directory.")
                    bcioslog.append(fr"Syscall [wr {targetfile}] - '{targetfile}' doesnt exist.")
            else: 
                bcioslog.append(fr"Syscall [wr {targetfile}] - Acces Denied (guest account)") 
                print("[CatError 003] You do not have permission to edit files.")
        
        elif inp.startswith("run"):
            if files.get("usr.conf")["content"] != r"guest@guest \0" or ignore == True:
                targetfile = inp[4:].strip()
                try:
                    thefile = files.get(targetfile)["content"]
                    if thefile.startswith("!CAT"):
                        codetarget = thefile[5:]
                        toprint = files.get(codetarget)["content"]
                        print(toprint.removesuffix(r"\0") if toprint.endswith(r"\0") else toprint)
                    elif thefile.startswith("!RM"):
                        codetarget = thefile[4:]
                        files.pop(codetarget)
                    elif thefile.startswith("!echo"):
                        thefile = thefile.replace("_user_", user["privilege"])
                        print(thefile[6:])
                    elif thefile.startswith("!crt"):
                        codetarget = thefile[5:]
                        if codetarget in files:
                            print(f"[CatError 001] The target file already exists.")
                        else:
                            files[codetarget] = { "content" : "" }
                    elif thefile.startswith("!wr"):
                        payload = thefile[4:].strip()
                        start_pos = payload.find(r"\1")
                        end_pos = payload.find(r"\0", start_pos)

                        if start_pos != -1 and end_pos != -1:
                            codetarget = payload[:start_pos].strip()
                            content_start = start_pos + len(r"\1")
                            newcontent = payload[content_start:end_pos].strip()

                            if codetarget in files:
                                files[codetarget]["content"] = newcontent
                            else:
                                print(f"[CatError 002] There is no file named {codetarget} in the current directory.")

                        else: print(f"[CathMError 001] CatSyntaxError in {targetfile}: Missing or misplaced delimiters.") 
                    
                except (NameError, KeyError, TypeError):
                    print(f"[CatError 002] There is no file named {targetfile} in the current directory.")
            else: print("[CatError 003] You do not have permission to execute scripts.")

        elif inp == "user":
            print(f"Current user: {user['privilege']}")

        elif inp == "user -priv":
            print(f"{user['privilege']}@{user['name']}")

        elif inp == "netuser":
            for i in files.get("users.conf")["content"]:
                print(i)

        elif inp == "logout":
            print(f"Logging out from {user['privilege']}@{user['name']} account...")
            guestacc = r"guest@guest \0"
            print(guestacc)
            files["usr.conf"]["content"] = guestacc
            

        elif inp.startswith("login"):
            if files.get("usr.conf")["content"] == r"guest@guest \0":
                parts = inp.split()
                if len(parts) == 2:
                    name = parts[1]
                    if name not in files.get("users.conf")["content"]:
                        print(f"[CatError 005] There is no user named {name}.")
                    else:
                        typeduser = files.get("users.conf")["content"]
                        for stored_key in typeduser.keys():
                            if stored_key == name:
                                password = input(f"Enter the password for {name}: ")
                                if password == files.get("passwords.conf")["content"].get(name):
                                    print(f"Successfully logged in as {name}.")
                                    files["usr.conf"]["content"] = fr"{name}@{files.get('users.conf')['content'][name]} \0"
                                else:
                                    print("[CatError -006] Incorrect password.")
            else: print("[CatError -001] You must be logged out (guest account) to be able to log in.")

        elif inp == "123":
            print("123")
            ignore = True

        elif inp == "321":
            print("321")
            ignore = False

        elif inp == "cls":
            for i in range(100):
                print("\n")

        elif inp == "license":
            print("CatoSoft CatOS [Version 0.1 Indev]")
            print("CatoSoft CathM [Version 0.1 Compat]")
            print("(c) CatoSoft Corporation. All rights reserved.")
            print("Cats General Public License - CGPL")
            print("You can run, share and modify CatOS freely, yet we want to be credited for it.")
            print("You can use CatOS for free, either personal or commercial use.")
            print("If u made a modification for CatOS, you must license it under Cats General Public License.")
            print("The developers of CatOS DON'T CARE for any of ur problems you make using CatOS.")

        elif not inp.strip():
            continue

        elif inp == "ifconfig":
            print("CatOS IP Configuration")
            print("LAN adapter: Unknown")
            print("MAC Address: Unknown")
            print("IP Address: Unknown")
            print("The networking features aren't fully available yet.")

        else:
            print(f"[CatError 000] The command {inp} isnt a valid command.")
            continue

    input()
    print("BCIOS/UEFI Recovery mode")
    print("")
    print("1 - View BCIOS log")
    print("2 - Restart CatOS")
    print("3 - Advanced Reconfiguration of .conf files.")
    while recovery:
        inp = input("BIOS>").strip()
        if inp == "1":
            print(f"BCIOS Log: ")
            time.sleep(0.4)
            print(f"Searching... {len(bcioslog)} notes.")
            for part in bcioslog:
                print(part.removesuffix('\n'))
                time.sleep(random.randint(1, 2) / 10)

        elif inp == "2":
            choice = input("Are you sure, ALL YOUR DATA WILL BE LOST (y/n):")

            if choice == "n":
                print("Cancelling CatOS restart...")
                time.sleep(0.1)
                continue
            elif choice == "y":
                print("Restarting CatOS...")
                time.sleep(2)
                print("This might take a while...")
                time.sleep(5)
                recovery = False
                break
            else:
                print("Please enter 'y' or 'n'.")

        elif inp == "3":
            print("Troubleshooting...")
            time.sleep(1)
            try:
                print("usr.conf misconfigured: ", files.get("usr.conf")[content])
            except Exception:
                continue

            try:
                files["usr.conf"][content] = r"restoredacc@user \0"
                time.sleep(2)
            except Exception:
                files["usr.conf"] = {"content" : r"restoredacc@user \0"}
                time.sleep(3)
            recovery = False
