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


#connection.enable()
output = connection.send_config_from_file('cisco_telnet_set_file.txt')
print(output)

connection.disconnect()
