import myserial

console = myserial.open_console()
myserial.run_command(console)
myserial.run_command(console, 'show chassis hardware', sleep=3)
output = myserial.read_from_console(console)
print(output)