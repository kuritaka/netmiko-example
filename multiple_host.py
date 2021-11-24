from netmiko.ssh_dispatcher import ConnectHandler
from datetime import datetime

start_time = datetime.now() 
print(start_time)

cisco1 = {
    'device_type': 'cisco_ios',
    'host':   'cisco1',
    'username': 'cisco',
    'password': 'cisco123',
}

cisco2 = {
    'device_type': 'cisco_ios',
    'host':   'cisco2',
    'username': 'cisco',
    'password': 'cisco123',
}

all_devices = [cisco1, cisco2] 


start_time = datetime.now()

for a_device in all_devices: 
    net_connect = ConnectHandler(**a_device) 
    output = net_connect.send_command("show arp") 
    print(f"\n\n--------- Device {a_device['device_type']} ---------") 
    print(output) 
    net_connect.disconnect()
    print("--------- End ---------") 
 
end_time = datetime.now() 
total_time = end_time - start_time  
