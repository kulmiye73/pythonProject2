import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='10.0.0.229', username='pi',password="")

stdin, stdout, stderr = ssh.exec_command('ip addr show')
#stdin, stdout, stderr = ssh.exec_command('sudo apt update && sudo apt upgrade -y')
for line in stdout.read().splitlines():
    print(line)

ssh.close()
