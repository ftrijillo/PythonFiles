from netmiko import ConnectHandler
import getpass
import re
import datetime

now = datetime.datetime.now()
today = str(now.year) + "-" + str(now.month) + "-" + str(now.day)

password = getpass.getpass(prompt="Enter password: ")

juniper_device = {
    'device_type': 'juniper_junos',
    'ip': '10.250.0.52',
    'username': 'ftrijillo',
    'password': password,
    'port': 22,
    'verbose': True
}
print('Connecting to ' + juniper_device['ip'])
connection = ConnectHandler(**juniper_device)

output = connection.send_command('show configuration | display set')
prompt = connection.find_prompt()
match = re.search("[0-9a-z]+\@([0-9A-Z\-]+).+", prompt)
hostname = match.group(1)

filename = today + "-" + hostname + ".txt"
with open(filename, 'w') as backup:
    backup.write(output)
    print('Backup of ' + hostname + ' completed successfully')
    print ('=' * 30)

connection.disconnect()