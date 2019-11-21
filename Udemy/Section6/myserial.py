import serial
import time

def open_console(port='/dev/tty.usbserial-A106QIEL', baudrate=9600):
    console = serial.Serial(port=port, baudrate=baudrate, parity='N', stopbits=1, bytesize=8, timeout=8)
    if console.isOpen():
        return console
    else:
        return False

def run_command(console, cmd='\n', sleep=1):
    print('Sending command: ' + cmd)
    console.write(cmd.encode() + b'\n')
    time.sleep(sleep)

def read_from_console(console):
    bytes_to_read = console.inWaiting()
    if bytes_to_read:
        output = console.read(bytes_to_read)
        return output.decode()
    else:
        return False