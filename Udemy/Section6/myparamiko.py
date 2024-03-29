import paramiko
import time

def connect(server_ip, server_port, user, pswd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server_ip, port=server_port, username=user, password=pswd, look_for_keys=False, allow_agent=False)
    return client

def get_shell(client):
    connection = client.invoke_shell()
    return connection

def send_command(connection, command):
    connection.send(command + '\n')
    time.sleep(2)
    output=connection.recv(19200)
    return output

def close(client):
    if client.get_transport().is_active():
        client.close()