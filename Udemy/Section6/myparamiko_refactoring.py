import myparamiko

ssh_client=myparamiko.connect('10.1.10.200', 22, 'ftrijillo', 'Ratajoa786!')
remote_connection = myparamiko.get_shell(ssh_client)
myparamiko.send_command(remote_connection, 'set cli screen-length 0')
output = myparamiko.send_command(remote_connection, 'show configuration | display set')
version = myparamiko.send_command(remote_connection, 'show version')
print(output.decode())
print(version.decode())
myparamiko.close(ssh_client)
