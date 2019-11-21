import myparamiko as myp
import datetime

devices = ['10.1.10.200']

for device in devices:
    ssh_client = myp.connect(device, 22, 'ftrijillo', 'Ratajoa786!')
    remote_connection = myp.get_shell(ssh_client)
    myp.send_command(remote_connection, 'set cli screen-length 0')
    output = myp.send_command(remote_connection, 'show configuration | display set')

    output_str = output.decode()
    #print(output_str)

    list = output_str.split('\n')
    list = list[1:-1]

    config = '\n'.join(list)
    print(config)

    now = datetime.datetime.now()
    today = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
    file = device + '-' + today + '.txt'
    with open(file, 'w') as f:
        print("Saving configuration: " + file)
        f.write(config)
    
    myp.close(ssh_client)