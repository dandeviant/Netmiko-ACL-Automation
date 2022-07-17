from netmiko import ConnectHandler

cisco = {
	'device_type': 'cisco_ios',
	'host': '192.168.124.133',
	'username': 'cisco',
	'password': 'cisco',
	'port': 22,
	'secret': 'cisco',
}




net_connect = ConnectHandler(**cisco)
net_connect.enable()

commands = ['access-list 10 permit any']

config = net_connect.send_config_set(commands)
print("{}\n".format(config))

output = net_connect.send_command('show access-list')
print("{}\n".format(output))
