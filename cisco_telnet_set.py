from netmiko.ssh_dispatcher import ConnectHandler
from datetime import datetime

start_time = datetime.now() 
print(start_time)

connection = ConnectHandler(host='11.11.11.11',
                            username='cisco',
                            password='cisco123',
                            device_type='cisco_ios_telnet'
                            )

connection = ConnectHandler(**test1)

config_commands = [
    'interface  gi3/0/37',
    'description test'
    ]

connection.enable()
output = connection.send_config_set(config_commands)
print(output)

connection.disconnect()
