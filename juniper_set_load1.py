from netmiko.ssh_dispatcher import ConnectHandler
from datetime import datetime

connection = ConnectHandler(ip='11.11.11.11',
                            username='juniper',
                            password='juniper',
                            device_type='juniper'
                            )

connection = ConnectHandler(**test1)


connection.send_config_from_file("juniper_set_load1.conf")
connection.commit()

connection.disconnect()