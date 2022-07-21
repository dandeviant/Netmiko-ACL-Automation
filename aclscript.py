from netmiko import ConnectHandler
import time


admin = {
	'device_type': 'cisco_ios',
	'host': '192.168.100.1',
	'username': 'cisco',
	'password': 'cisco',
	'port': 22,
	'secret': 'cisco',
}

library = {
	'device_type': 'cisco_ios',
	'host': '192.168.4.2',
	'username': 'cisco',
	'password': 'cisco',
	'port': 22,
	'secret': 'cisco',
}

academic = {
	'device_type': 'cisco_ios',
	'host': '192.168.3.1',
	'username': 'cisco',
	'password': 'cisco',
	'port': 22,
	'secret': 'cisco',
}

acl_admin = [
	'ip access-list extended 110',
	'deny icmp any 192.168.100.0 0.0.0.255 echo',
	'permit icmp any 192.168.100.0 0.0.0.255 echo-reply',
	'permit ip any any',
	'exit',
	'int fa3/0',
	'ip access-group 110 out',
	'end',
]

acl_library = [
	'ip access-list extended 120',
	'deny icmp 192.168.110.0 0.0.0.255 192.168.120.0 0.0.0.255 echo',
	'permit icmp 192.168.110.0 0.0.0.255 192.168.120.0 0.0.0.255 echo-reply',
	'permit icmp 192.168.100.0 0.0.0.255 192.168.120.0 0.0.0.255',
	'permit ip any any',
	'exit',
	'int fa0/0',
	'ip access-group 120 out',
	'end',
]


cont = "1"
print(" Netmiko ACL Automation Script")
print(" =============================")
print(" Routers: Cisco 7200\n")
print(" Access-Control Lists to apply:\n")
print(" =============== admin-router ===============")
print(" 1. Block all inbound ping targeting Admin network (192.168.100.0)")
print(" 2. Allowing outbound ping from Admin network\n")
print(" =============== library-router ===============")
print(" 1. Block inbound ping from Academic network (192.168.110.0)")
print(" 2. Allow inbound ping from Admin network (192.168.100.0)")
print("\n")

time.sleep(2)

print("==============================")
print("Configuring admin-router")
print("==============================\n")
net_connect = ConnectHandler(**admin)
net_connect.enable()

print("\n====== show run | include hostname ======")
hostname = net_connect.send_command('show run | include hostname')
print("{}".format(hostname))
time.sleep(1)
print("\n====== Configuring ACL =====")
config = net_connect.send_config_set(acl_admin)
print("{}\n".format(config))
time.sleep(2)
print("====== sh access-list ======")
test = net_connect.send_command('sh access-list')
print("{}".format(test))
time.sleep(1)

print("\n")
print("==============================")
print("Configuring lbrary-router")
print("==============================\n")
net_connect = ConnectHandler(**library)
net_connect.enable()

print("\n====== show run | include hostname ======")
hostname = net_connect.send_command('show run | include hostname')
print("{}".format(hostname))
time.sleep(1)
print("\n====== Configuring ACL =====")
config = net_connect.send_config_set(acl_library)
print("{}\n".format(config))
time.sleep(2)
print("====== sh access-list ======")
test = net_connect.send_command('sh access-list')
print("{}".format(test))
net_connect.disconnect()
time.sleep(1)

print("\n\nACL configuration completed.")
print("Exiting script")
time.sleep(2)

