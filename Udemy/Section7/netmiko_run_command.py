from netmiko import Netmiko 
from netmiko import ConnectHandler
import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

#connection = Netmiko(host='10.1.10.200', username='ftrijillo', password='Ratajoa786!', device_type='juniper_junos')
juniper_device = {
    'device_type': 'juniper_junos',
    'ip': '10.1.10.200',
    'username': 'ftrijillo',
    'password': 'Ratajoa786!',
    'port': 22,
    'verbose': True
}

connection = ConnectHandler(**juniper_device)
#output = connection.send_command('show int terse')
#print(output)

prompt = connection.find_prompt()
print(prompt)

mode = connection.check_config_mode()
if not mode:
    connection.config_mode()

connection.send_command('set interface fe-0/0/3 description test_description')
connection.commit(confirm=False, comment='Commit Test', and_quit=True)
output = connection.send_command('show interface description')
print(output)

connection.disconnect()
