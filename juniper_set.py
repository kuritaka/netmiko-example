from netmiko.ssh_dispatcher import ConnectHandler
from datetime import datetime

start_time = datetime.now() 
print(start_time)

connection = ConnectHandler(host='11.11.11.11',
                            username='juniper',
                            password='juniper',
                            device_type='juniper'
                            )

connection = ConnectHandler(**test1)

config_commands = [
   'set system host-name test-host1',
   'set system max-configuration-rollbacks 49'
]

output = connection.send_config_set(config_commands)
print(output)

connection.disconnect()
