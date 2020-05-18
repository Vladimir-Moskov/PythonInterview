# 1. Monitoring and Troubleshooting Linux System Performance

# 1. Identifying System Resource Usage
cd /proc

ls -lah | less
ps aux | grep 78
ls -lah 78 | less
journalctl _PID=78
ls -p | grep -v / | column

less cpuinfo
less cpuinfo | grep processor
cat uptime
# or
uptime
# supportet filesystem types
less filesystems

# https://access.redhat.com/solutions/406773
less meminfo
free -k
free -h

# 2. Storage and Network Bandwidth Metrics
df -lah
df -t ext4
df -h | grep -v sys
# see inodes - amount free/used files count
df -ih
top
# network monitoring
apt-get install iftop
iftop
ip a
# from outside of the system
iftop -i eth0

# from inside of the system
apt-get install nethogs
nethogs eth0
curl https://www.pluralsight.com/

# 3. System Monitoring Solutions
apt-get install collectd
# collectd
# Nagios
# Munin
# Nmon
# cockpit

apt-get install cockpit
systemctl start cockpit
https://192.168.2.21:9090/dashboard

# 4. Controlling System Resource Usage


