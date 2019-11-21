import paramiko
import getpass
import time

password = getpass.getpass(prompt="Password: ")
ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('iad3-lr1.net', port=22, username='ftrijillo', password=password, look_for_keys=False, allow_agent=False)

remote_connection = ssh_client.invoke_shell()
remote_connection.send("set cli screen-length 0\n")

ping_to = raw_input("Address to ping: ")
ping_from = raw_input("Address to ping from: ")

remote_connection.send('ping ' + ping_to + ' source ' + ping_from + ' rapid count 100\n')
time.sleep(10)
ping_output = remote_connection.recv(4096)
print "{code:title='devicename'}\n" + ping_output.decode('utf-8') + "{code}"

remote_connection.send('show isis adj\n')
time.sleep(5)
isis_output = remote_connection.recv(4096)
print "{code:title='devicename'}\n" + isis_output.decode('utf-8') + "{code}"

ssh_client.close()