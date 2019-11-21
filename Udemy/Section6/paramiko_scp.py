import paramiko
from scp import SCPClient

ssh_client = paramiko.SSHClient()
ssh_client.load_system_host_keys()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('10.1.10.200', port=22, username='ftrijillo', password='Ratajoa786!', look_for_keys=False, allow_agent=False)

scp = SCPClient(ssh_client.get_transport())

#scp.put('10.1.10.200-2019-10-9.txt', '/var/tmp/newfile.txt')

#Copy a directory
#scp.put('directory1', recursive=True, remote_path='/var/tmp')

scp.get('/var/tmp/directory1/10.1.10.200-2019-10-9.txt', 'copiedfile.txt')
scp.close()