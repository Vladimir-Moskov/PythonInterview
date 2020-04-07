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

shutdown -r
shutdown -h now
shutdown -h +60
powerof
init 0
init 6

########################################
# Linux Sysadmin Basics 03 -- Text Editors (and review of basic commands)
# https://www.youtube.com/watch?v=fEGSA68uAR4


