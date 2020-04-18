########################################
# Linux Sysadmin Basics 02 -- Basic Commands
# https://www.youtube.com/watch?v=Lbh8Bh_SEzU&t=3s

pwd

cd
cd ..

ls
ls -a
ls *

mkdir new_dir
mkdir new_dir/new_subdir
mkdir -p new_dir2/new_subdir2 # create recursively

touch new_file.txt
mv new_file.txt new_dir/
touch new_dir/new_file2.txt
mv new_dir/new_file2.txt new_dir/new_subdir/

rm new_dir
rm -r

man
man man

top
top -v
htop
htop -v
########################################
# Linux Sysadmin Basics 02.1 -- More Basic Commands
# https://www.youtube.com/watch?v=ZeZVkA1zjWg&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=5

echo $EDITOR
nano script2.py
ln -s script2.py linkToScript2

head linkToScript2
tail -f script2.py
more

shutdown -r
shutdown -h now
shutdown -h +60
powerof
init 0
init 6

#######################################
# Linux Command-Line for Beginners: What's happening on this machine?
# https://www.youtube.com/watch?v=EbOEqycEFeM&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=6

w
who
netstat -tupln
man netstat

########################################
# Linux Sysadmin Basics 03 -- Text Editors (and review of basic commands)
# https://www.youtube.com/watch?v=fEGSA68uAR4

cp
cat 1 2
nano
vi
man vi
emacs

########################################
# Linux Sysadmin Basics 04 -- Shell Features -- Pipes and Redirection
# https://www.youtube.com/watch?v=-Z5tCri-QlI&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=8

echo "another line stream as override" > next_file.txt
echo "another line stream as append" >> next_file.txt

ls -alh >> listoutput

ls -alh errortrigername 2>  listoutputerror
mail -s "subject metter" vova < listoutputerror
sudo apt-get install mailutils

ps aux
# pagenation
ps aux | less

########################################
# Linux Sysadmin Basics 4.1 -- Filtering Output and Finding Things (&&, cut, sort, uniq, wc, grep)
# https://www.youtube.com/watch?v=nLa6jAbULe8&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=9

# logical AND = && program run
ls .. && echo "command .. has been sucsessfully executed"

# cut = split str content, where d - delimiter, f2 - second field
cat file.txt | cut -d: -f2

# Hacker rank CUT chalanges
# get 3rd char from line
cut -c3
# The output should contain lines. Each line should contain just two characters at the and
# the position of the corresponding input line.
cut -c2,7
# Each line should contain the range of characters starting at
# the position of a string and ending at the position (both positions included).
cut -c2-7
# The output should contain N lines. Each line should contain just the
# first four characters of the corresponding input line.
cut -c1-4
# Given a tab delimited file with several columns (tsv format) print the first three fields.
cut -f-3
# Print the characters from thirteenth position to the end.
cut -c13-
# fron 3rd word to the end
cut -d" " -f4-



# sort file lines, b - ignore white spaces, f - case insensative
cat file.txt | sort -bf

# uniq only lines
cat file.txt | uniq

# file info
wc file.txt

# grep filter/search
cat file.txt | grep search_word
grep search_word file.txt
grep search_word ./* | uniq | cut -d: -f1

########################################
# https://www.youtube.com/watch?v=8P-Vek7Vtgg&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=10
# Linux Sysadmin Basics 05 -- Package Management with apt-get

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install val
apt-cache search tmux
cat /etc/apt/sources.list

sudo apt-get remove

########################################
# https://www.youtube.com/watch?v=8SkN7UofOww&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=11
# Linux Sysadmin Basics -- Linux File Permissions

touch another.txt
ls -l
chmod 777 another.txt
ls -l
chmod 640 another.txt
ls -l


# apply default mask
chmod xxx -r dir
nano /etc/login.defs

#  change owner  user:group
chown root another.txt
chown vova:vova another.txt

########################################
# https://www.youtube.com/watch?v=WhCIuGjhH-0&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=12
# Basic Linux Access Control

# usr info
id
whoami

########################################
# https://www.youtube.com/watch?v=UN1QB5BIvps&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=13
# Linux Sysadmin Basics -- User Account Management

sudo -i
tail /etc/passwd
cat /etc/passwd | wc -l
tail /etc/shadow
cat /etc/group

# add user , -m create home dir, -d /home/vavas, -u user id, -g group id, -s /bin/bash - set shell
# useradd -m -d /home/vavas -u 1044 -g 44
useradd -m -d /home/vavas  -s /bin/bash vavas
ls /home

# new user skeleton for file system
ls /etc/skel
ls -l /home/
grep vavas /etc/group
# set user password
passwd vavas

# lock account
usermod -L vavas
# unlock account
usermod -U vavas
# delete user
userdel deluser
rm -rf /home/deluser
# batch user creation
man newusers

#####################################################
# Linux Sysadmin Basics -- 6 -- Processes Overview
# https://www.youtube.com/watch?v=ls5cGi12kGw&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=14

env
# disk space
df -h
# disk usage
du
# go to prev dir
cd -

# copy text to the clipboard
cat file.txt | xclip -selection clipboard

#####################################################
# Linux Sysadmin Basics -- 6.1 Process Signals
# https://www.youtube.com/watch?v=lP7xoqkqDZQ&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=15

kill pid
# list kill options
kill -l
kill 829 # vi

ps aux | grep nano
# 15 is default
kill -15  829
# 9 is hard kill
kill -9  829

ps aux | grep cups
sudo killall cupsd

#
man pgrep
man pkill
man signal


#####################################################
# Linux Sysadmin Basics -- 6.2 State, Niceness, and How to Monitor Processes
# https://www.youtube.com/watch?v=vsEJz9aKGKU&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=16

# dafault order by cpu
top

#  nice - run a program with modified scheduling priority
man nice
nice -n 15 run_process

# renice - alter priority of running processe by PID
renice -5 789

#####################################################
# Linux Sysadmin Basics -- 6.3 The /proc Filesystem
# https://www.youtube.com/watch?v=0XdjODvsRN8&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=17


ls /proc -la
# virtual file systtem - report file system disk space usage
df -ah
ls /proc -lah
ls -lah /proc/1/
cd  /proc
cd 1
# comand line command name
cat cmdline
cat cwd
ls -al cwd
ls fd
# memoty map info
ls maps
# env variables
ls envos

cat statm

# strace - trace system calls and signals
man strace

#####################################################
# Linux Sysadmin Basics -- Filesystem Purpose and Absolute/Relative Pathnames
# https://www.youtube.com/watch?v=ar37viZGQwk&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=18

ls /dev
ps -aux | grep udevd
df -ah
ifconfig
/sbin/ifconfig

#####################################################
# Linux Sysadmin Basics -- 7 -- Filesystem Layout Overview
# https://www.youtube.com/watch?v=svh8sSuz5BI&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=19

ls -lah /

# place for configs
ls -lah /etc
ls -lah /etc/shh

# secure sys bin
ls /sbin | less
# all other binaries
ls /bin | less
# temp files
ls /tmp
# users home
ls /home
# shared libs under lib and lib64
ls /lib | ls /lib64
# file system description
man hier

#####################################################
# Linux Sysadmin Basics -- 7.1 Filesystem Layout
# https://www.youtube.com/watch?v=TG5YJe9camA&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=20

ls /
# kernel and boot loader
ls /boot -lah
# all devices in
ls -lah /dev
# mounted devises or filesystems
ls /media
ls /mnt
# optional soft
ls /opt
# logs, variables
ls /var

#####################################################
# Linux Sysadmin Basics -- Linux File Types
# https://www.youtube.com/watch?v=EDgkcvOoY8A&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=21

#####################################################
# Linux Basics -- Scheduling Tasks with Cron
# https://www.youtube.com/watch?v=8j0SWYNglcw&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=22

crontab -l
login vova
# edit cron jobs
crontab -e

# 15 10 * * 3-5   echo "$(date): checking in." >> /var/log/mycheckin
# (m)(h)(dom)(moy)(wd)   (cmd)
# * * * * *  echo "hi there" >> ~/hi.txt
ls /var/spool/cron/crontabs
cat /var/spool/cron/crontabs/vova
ls /etc/cron.d/
# system tasks
sudo /etc/crontab
cat /etc/cron.allow
# edit user cron tasks
crontab -e -u vova


#####################################################
# Basic tmux Tutorial - Windows, Panes, and Sessions over SSH
# https://www.youtube.com/watch?v=BHhA_ZKjyxo&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=25
# Basic tmux Tutorial, Part 2 -- Shared Sessions
# https://www.youtube.com/watch?v=norO25P7xHg&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=26

# session management
tmux ls (or tmux list-sessions)
tmux new -s session-name
Ctrl-b d Detach from session
tmux attach -t [session name]
tmux kill-session -t session-name

Ctrl-b c Create new window
Ctrl-b d Detach current client
Ctrl-b l Move to previously selected window
Ctrl-b n Move to the next window
Ctrl-b p Move to the previous window
Ctrl-b & Kill the current window
Ctrl-b , Rename the current window
Ctrl-b q Show pane numbers (used to switch between panes)
Ctrl-b o Switch to the next pane
Ctrl-b ? List all keybindings

# moving between windows
Ctrl-b n (Move to the next window)
Ctrl-b p (Move to the previous window)
Ctrl-b l (Move to the previously selected window)
Ctrl-b w (List all windows / window numbers)
Ctrl-b window number (Move to the specified window number, the
default bindings are from 0 -- 9)

# Tiling commands
Ctrl-b % (Split the window vertically)
CTRL-b " (Split window horizontally)"
Ctrl-b o (Goto next pane)
Ctrl-b q (Show pane numbers, when the numbers show up type the key to go to that pane)
Ctrl-b { (Move the current pane left)
Ctrl-b } (Move the current pane right)
Ctrl-d : (close pane)

# Make a pane its own window
Ctrl-b : "break-pane"

# add to ~/.tmux.conf
bind | split-window -h
bind - split-window -v

##########################
# Open SSH for windows ubuntu subsystem
"
    sudo apt-get purge openssh-server
    sudo apt-get install openssh-server
    sudo nano /etc/ssh/sshd_config and disallow root login by setting PermitRootLogin no

    Then add a line beneath it that says:

    AllowUsers yourusername

    and make sure PasswordAuthentication is set to yes if you want to login using a password.

    Disable privilege separation by adding/modifying : UsePrivilegeSeparation no

    sudo service ssh --full-restart

    Connect to your Linux subsystem from Windows using a ssh client like PuTTY.
"

#####################################################
# Archiving and Compression on Linux - Basic tar Commands
# https://www.youtube.com/watch?v=tSRlNwaUgPQ&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=27

tree .
# archive
tar -zcvf gitProj.tar.gz vova/git_project/
mv gitProj.tar.gz decompresion_chamber/
# dearchive
tar -zxf gitProj.tar.gz
# tar bomb
cd git_project/
tar -zcvf ../tarbomb.tar.gz .

#####################################################
# Bash Scripting 2 -- Bash Basics
# https://www.youtube.com/watch?v=4-hw6DPBlsw&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=29


echo "hellow Linux man" > hello.txt
cat  hello.txt
echo "What!!! Linux man!!!" >> hello.txt
wc -l < hello.txt
(cat  hello.txt |  wc -l) && echo "Done" >>  hello.txt
ls "wrong_file" && echo "sucsess"
ls "wrong_file" || echo "sucsess?"
ls "wrong_file" 2>>  hello.txt

#####################################################
# https://www.youtube.com/watch?v=MYWvVgIL_Ys&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=30
# Bash Scripting 3 -- Variables and Quoting

# varables
echo $HOME
my_var="the best variable"
echo $my_var
new_number=7
echo $new_number
echo "The very rundom number = $new_number, ;)"
old_number=482
echo "The value ${old_number}th"
echo "Ther are X lines in the /etc/shadow"
wc -l < /etc/shadow
echo "Ther are X lines in the /etc/group"
wc -l < /etc/group
echo "Ther are `wc -l < /etc/group` lines in the /etc/group"
num_lines=`wc -l < /etc/shadow`
echo "Ther are ${num_lines} lines in the /etc/shadow"


#####################################################
# https://www.youtube.com/watch?v=U2_MvxnqLRE&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=31
# Bash Scripting 4 -- How Bash Scripts Work

# which - locate a command
which bash

# bashScript.sh
chmod +x bashScript.sh
./bashScript.sh
bash bashScript.sh
# execute script in current login shell / inline execution
source bashScript.sh
. bashScript.sh

echo $message

#####################################################
# https://www.youtube.com/watch?v=Vbu8rfVaABw&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=32
# Bash Scripting 5 -- Arguments


#  In real life, this is something like 'tar zcf filename.tar.gz directory'
#  ('zcf', 'filename.tar.gz', and 'directory' are the arguments in this example).
#
#  $# -- number of args that our script was run with
#  $0 -- the filename of our script
#  $1..$n -- script arguments

#####################################################
# https://www.youtube.com/watch?v=VMZBFjYgjR4&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=33
# Bash Scripting 6 -- 'If' and Testing

# https://www.youtube.com/watch?v=9EfN5clA710&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=34
# Bash Scripting 7: Functions and Course Review

#####################################################
# https://www.youtube.com/watch?v=rJMFxIbDe-g&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=35
# Everything You Need to Know About $PATH in Bash


# How does Linux know where to look for the commands that you type at the command-line? In this video you'll
# learn how the $PATH variable works in Linux. Specifically, we'll look at how this value is looked up in bash,
# and how you can modify it.
#
# I'll also introduce you to the `which` command, which you can use to check which filepath bash is using for a
# given name (executable).
#
# To modify PATH for
# -a single user (normal or root): /home/username/.bash_profile
# -all users except root: /etc/profile

which sudo
echo $PATH
# update $PATH - normal way, append
PATH=$PATH:/some/dir
# redirect lookup order - prepend
PATH=/root:$PATH

# that is way - use full path in bash scripts
ls -lah /etc/
cat  /etc/profile

# change path on user level
ls /home/vova/.bash_profile

#####################################################
# https://www.youtube.com/watch?v=tweyWNr6X18&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=36
# The Linux 'script' Command: Record Your Shell Sessions

# Simplest Way to Log Shell Sessions
script simplescript.log

# A single command
script -c 'netstat -tupln' netstat.log

# Add timing information, so you can replay the shell session later
script myscript.log --timing=time.log

# Replay a captured shell session (with timing info)
scriptreplay -s myscript.log --timing=time.log
scriptreplay -s myscript.log -t time.log

# to start record shell session
script
# to end session
Ctrl+D
# or just
exit
# specify file name
script myscript.log
# add timing log
script myscript.log --timing=time.log

# view recording
scriptreplay -s myscript.log -t time.log

#####################################################
# https://www.youtube.com/watch?v=vz2DGSBBpXg&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=37
# Linux Shell Aliases: What You Need to Know

# always on shell session level until has not saved in .bash_aliases on root or user level
# to see all alias
alias
# as helper
alias lr="ls -lrc"
# as shawing
alias ls="ls -a --color"
# or redirecting
alias vim="nvim"
alias lr="ls -lrah"
# but do not forget check first
alias | grep "lr"
# unset/delete alias
unalias lr

#####################################################
# 8 Basic lsof Commands Every Sysadmin Needs to Know
# https://www.youtube.com/watch?v=rLgRkjM7amo&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=38

# sof basics - list open files on Linux and Unix (expand for timestamps and details).
#
# In this video I introduce the 'lsof' command, found on Linux and Unix systems.
# I'll show you some practical examples and teach you how to explore what's
# happening with the filesytem in a system or process.

# Which files are open?
lsof
# Which processes have this file open?
lsof /var/log/nginx-error.log
# Which files does process X have open?
lsof -p 1
lsof -p `pgrep ABC`
# Where is the binary for this process?
lsof -p ABC | grep bin
#  Which shared libraries is this program using? (manually upgrading software, i.e. openssl)
lsof -p PID | grep .so
# Where is this thing logging to?
lsof -p ABC | grep log
# Which processes still have this old library open?
lsof grep libname.so
# Which files does user XYZ have open?
lsof -u XYZ
lsof -u XYZ -i # network only
# Which process is listening on Port X (or using Protocol Y)?
lsof -i :80
lsof -i tcp
lsof -i udp
# Super lsof Story Time!

lsof | head
netstat -tupln
# curl - transfer a URL
curl localhost
ps aux

#####################################################
# https://www.youtube.com/watch?v=wiRt3mY7Rrw&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=39
# Monitoring Linux Systems and Services with Monit (Hands-On Linux Course Preview)
# !!! retry

apt-get install monit
# start monit at boot
systemctl enable monit
# start it
systemctl start monit
nano /etc/monit/monitrc
cd /etc/monit/
mv monitrc monitrc-old

# Linux System Monitoring with Monit, part 2: SSH Local Forwarding for our Web Dashboard
# https://www.youtube.com/watch?v=ThcaW4MVGLY&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=40

#You can use this same SSH feature (local forwarding) to access services that are hidden from the public Internet by a
#firewall, local network, etc. If you can get to a server with SSH, you can 'see from its perspective'
# on your local machine, by mapping individual ports on the server to your local machine.

#####################################################
# https://www.youtube.com/watch?v=JX2lxKJC6yI&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=41
# Service Management with systemd (Hands-On Linux Course Preview)

systemd
systemctl status mysql
journalctl

#####################################################
#
# Top 10 Linux Job Interview Questions

# How to check the kernel version of a Linux system?
uname
uname -a
# How to see the current IP address on Linux?
ifconfig -a # -v
ip addr show
# How to check for free disk space in Linux?
df -ah
# How to see if a Linux service is running?
systemd
service udev (servicename) status/start/status pid
systemctl status udev (servicename)
# How to check the size of a directory in Linux?
du -sh /home
# How to check for open ports in Linux?
netstat -tulpn
# How to check Linux process information (CPU usage, memory, user information, etc.)?
ps aux | processname
top
# How to deal with mounts in Linux
ls /mnt
mount /dev/dsa2 mnt
cat /etc/fstab
# Man pages
# Other resources

#####################################################
# https://www.youtube.com/watch?v=59jnWX_EzTY&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=45
# Linux Documentation In

man
info
whatis ls
apropos python
#  recreate man
sudo mandb
ls /usr/share/doc
A list of Linux resources (and the context/info you need to use them) that will help you troubleshoot, learn new things, and find answers to questions you have while using Linux.

1:09 Man pages: man $COMMAND
4:09 Info pages: info $COMMAND

5:39 whatis $command
6:31 apropos $searchterm

whatis and apropos require 'sudo mandb' to be run before they work.

8:14 /usr/share/doc -- package-provided documentation

9:18 - Reddit
https://www.reddit.com/r/sysadmin/
https://www.reddit.com/r/linux/
https://www.reddit.com/r/freebsd/

10:11 - The Arch Linux Wiki
https://wiki.archlinux.org/index.php/...
https://wiki.archlinux.org/index.php/...

12:03 Bash Docs: http://www.tldp.org/LDP/abs/html/abs-...
13:07 Serverfault (sysadmin): http://serverfault.com
13:51 Stack overflow (programming): http://stackoverflow.com/

14:22 Official Documentation!
15:13 Use a search engine: Google, Duckduckgo, etc.

15:42 IRC: https://webchat.freenode.net/

18:50 Tech News/Article Aggregators:
news.ycombinator.com
https://lobste.rs/


