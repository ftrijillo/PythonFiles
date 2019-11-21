import paramiko

ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('10.1.10.200', port=22, username='ftrijillo', password='Ratajoa786!', look_for_keys=False, allow_agent=False)

remote_connection = ssh_client.invoke_shell()
remote_connection.send("set cli screen-length 0\n")
remote_connection.send('show interface terse\n')
#remote_connection.send('ping 10.1.10.1 rapid count 100')

import time
time.sleep(5)

output = remote_connection.recv(4096)
print("Output: \n", output.decode())

ssh_client.close()