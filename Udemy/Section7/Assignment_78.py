from netmiko import ConnectHandler

juniper_device = {
    'device_type': 'juniper_junos',
    'ip': '10.1.10.200',
    'username': 'ftrijillo',
    'password': 'Ratajoa786!',
    'port': 22,
    'verbose': True
}

connection = ConnectHandler(**juniper_device)
interface = raw_input('Enter interface to activate: ')
result = connection.send_command('show interface ' + interface + ' | match Phy')
if ('Physical interface') not in result:
    print 'You entered an invalid interface: ' + interface
elif ('Administratively down' in result):

    mode = connection.check_config_mode()
    if not mode:
        connection.config_mode()
    
    print 'Enabling interface ' + interface
    connection.send_command('delete interface ' + interface + ' disable')
    connection.commit(confirm=False, comment='Activate interface', and_quit=True)
    output = connection.send_command('show interface ' + interface + ' | match Phy')
    print(output)
else:
    print 'Interface ' + interface + ' is already activated.'
connection.disconnect()
