import getpass
import paramiko

IP = '106.10.57.110'
PORT = 1030


cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)

user = input("Username :")
pwd = getpass.getpass("Password :")

cli.connect(IP, port=PORT, username=user, password=pwd)
stdin, stdout, stderr = cli.exec_command('cat /proc/cpuinfo')
lines = stdout.readlines()
print(''.join(lines))

stdin, stdout, stderr = cli.exec_command('cat /proc/meminfo')
lines = stdout.readlines()
print("".join(lines))

cli.close() 