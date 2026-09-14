## CatOS

CatOS is a bit Unix-like OS, with understandble (i hope) commands and some buggy scripts and privilege system.
Written in Python, all the libraries are standard Python 3.14 libraries.

## Documentation of commands:
# crt
crt <filename>
is a commands to **cr**ea**t**e files.
All users except for guest can create files.
You cannot create a file with the same name as another file.

# rm
rm <filename>
is a command to delete (**r**e**m**ove)
all users except for guest can delete files.
There are also system files like passwords.conf, usr.conf, etc. 
To delete them you need to be root0 (Deleting system files may crash your CatOS or make it malfunction (if it aint obvious enough)).

# cat
cat <filename>
a command to read files.
All users except for guest can read files.

# wr
wr <filename>
a command to (over)**wr**ite files' contents.
All users can write files except for guest.
There are also system files like passwords.conf, usr.conf, etc. 
To overwrite them you need to be root0 (Overwriting system files may crash your CatOS or make it malfunction (if it aint obvious enough)).

# run
run <filename>
a command to run script files.
All users except for guest can run files.

# ls / list
ls / list
a command to list all files.
Everybody can do that.

# user
user
prints the active user name

# user -priv
user -priv
prints the active user *and* his privileges (guest, user or root0)

# netuser
netuser
prints all the user names on that machine

# logout
logout
logs out of the current user account (changes the user to guest)

# login
login <username>
A command to log in to another user account, can be only done if current account is guest.
After you type that command CatOS will ask for the password. 
All the passwords are stored in passwords.conf

# license
license

A fun command which prints out the Cats General Public License:

CatoSoft CatOS [Version 0.1 Indev]
CatoSoft CathM [Version 0.1 Compat]
(c) CatoSoft Corporation. All rights reserved.
Cats General Public License - CGPL
You can run, share and modify CatOS freely, yet we want to be credited for it.
You can use CatOS for free, either personal or commercial use.
If u made a modification for CatOS, you must license it under Cats General Public License.
The developers of CatOS DON'T CARE for any of ur problems you make using CatOS.

// CatoSoft Corporation is **not** a real company, the thing is just made so it looks cool.

## If you want to modify CatOS:
Commit your changes to a new branch, contributors will check the branches and if they like it they may merge the branch.
Please name the branches after your GitHub username and/or a quick overview of what you added (For example: CatOS Networking features by ...).
