from netmiko import ConnectHandler

r1 = {
    'device_type': 'cisco_ios',
    'ip': '10.10.10.1',
    'username': 'Ali',
    'password': 'Hojaji',
}
net_connect = ConnectHandler(**r1)

config_commands = ['router ospf 110', 'network 10.10.10.0 0.0.0.3 area 0', 'network 10.10.10.36 0.0.0.3 area 0']
output = net_connect.send_config_set(config_commands)
print(output)
