from netmiko.ssh_dispatcher import ConnectHandler
from datetime import datetime

start_time = datetime.now() 
print(start_time)

connection = ConnectHandler(ip='11.11.11',
                            username='cisco',
                            password='cisco123',
                            device_type='cisco_ios'
                            )

connection = ConnectHandler(**test1)

connection.disable_paging()

connection.enable()
output = connection.send_command(command_string='show run')
print(output)

connection.disconnect()

end_time = datetime.now() 
print(end_time)
total_time = end_time - start_time 
print(total_time)