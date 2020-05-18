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



