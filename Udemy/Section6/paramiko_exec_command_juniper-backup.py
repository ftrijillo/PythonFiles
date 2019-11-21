import myparamiko as myp

ssh_client = myp.connect('10.1.10.200', 22, 'ftrijillo', 'Ratajoa786!')
remote_connection = myp.get_shell(ssh_client)
myp.send_command(remote_connection, 'set cli screen-length 0')
output = myp.send_command(remote_connection, 'show configuration | display set')

output_str = output.decode()
#print(output_str)

list = output_str.split('\n')
list = list[1:-1]

config = '\n'.join(list)
print(config)

with open('router1-running-config.txt', 'w') as f:
    f.write(config)
    
myp.close(ssh_client)