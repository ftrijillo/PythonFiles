import myparamiko
import getpass

username = input("Username: ")
password = getpass.getpass(prompt="Password: ")

ssh_client = myparamiko.connect('127.0.0.1', 22, username, password)
remote_connection = myparamiko.get_shell(ssh_client)

myparamiko.send_command(remote_connection, 'sudo touch /Users/' + username + '/Dropbox/Bhaloo/Python_lvl2/Udemy/Section3_Part57/file1.txt')
myparamiko.send_command(remote_connection, password)
output = myparamiko.send_command(remote_connection, 'ls -al /Users/' + username + '/Dropbox/Bhaloo/Python_lvl2/Udemy/Section3_Part57')

print(output.decode())
myparamiko.close(ssh_client)
