import paramiko
import getpass
import time

IP = '106.10.57.110'
PORT = 1030

BUFSIZE = 65535

cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)

user = input("Username : ")
pwd = getpass.getpass('Password : ')

cli.connect(IP, port=PORT, username = user, password=pwd)
channel = cli.invoke_shell() #새로운 셀 세션 생성

channel.send('cat /proc/cpuinfo\n')
time.sleep(0.5)
channel.send('cat /proc/meminfo \n')
time.sleep(0.5)
channel.send('mkdir test_jimin\n')
time.sleep(0.5)
channel.send('cd test_jimin \n')
time.sleep(0.5)
channel.send('echo iot > iot.txt \n')
time.sleep(0.5)
channel.send('cat iot.txt\n')
time.sleep(0.5)


output = channel.recv(BUFSIZE).decode()
print(output)

cli.close()