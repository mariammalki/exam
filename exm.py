from netmiko import ConnectHandler


router = {
    'device_type': 'cisco_ios',
    'host': 'sandbox-iosxe-latest-1.cisco.com',
    'username': 'admin',
    'password': 'Cisco12345',
    'port': 22,
}

conn  = ConnectHandler(**router)

clock = conn.send_command("show clock")
print(clock)

interface = conn.send_command("sh ip int br")
with open ("interface.txt" , "w") as file: 
    file.write(interface)
print("interface.txt")
commande = [
      "interface loopback 8" ,
      "ip adress 10.8.8.8 255.255.255.248"
      "no shutdown"
]
configuration = conn.send_config_set(commands)
print(configuration)
