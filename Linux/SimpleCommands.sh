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
whiami

########################################
# https://www.youtube.com/watch?v=UN1QB5BIvps&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK&index=13
# Linux Sysadmin Basics -- User Account Management

sudo -i
tail /etc/passwd






