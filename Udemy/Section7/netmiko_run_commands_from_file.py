from netmiko import ConnectHandler

juniper_device = {
    'device_type': 'juniper_junos',
    'ip': '10.250.0.52',
    'username': 'ftrijillo',
    'password': 'YWiGCM3nuVe8F!dcw!FF',
    'port': 22,
    'secret': 'n/a',
    'verbose': True
}

connection = ConnectHandler(**juniper_device)

print('Entering config mode...')

print('Running commands from file...')
output = connection.send_config_from_file('juniper_commands.txt')
print(output)

connection.disconnect()