from netmiko import ConnectHandler

# Configuration du routeur
router = {
    'device_type': 'cisco_ios',
    'host': 'sandbox-iosxe-latest-1.cisco.com',
    'username': 'admin',
    'password': 'Cisco12345',
    'port': 22,
}

try:
    # Connexion au routeur
    net_connect = ConnectHandler(**router)
    print("Connexion établie avec le routeur.")

    # Afficher la date (show clock)
    show_clock = net_connect.send_command("show clock")
    print("Date et heure du routeur :")
    print(show_clock)

    # Afficher les interfaces dans un fichier interfaces.txt
    interfaces = net_connect.send_command("show ip interface brief")
    with open("interfaces.txt", "w") as file:
        file.write(interfaces)
    print("Les interfaces ont été sauvegardées dans 'interfaces.txt'.")

    # Configurer une interface loopback
    config_commands = [
        "interface loopback0",
        "ip address 10.8.8.8 255.255.255.240",
        "no shutdown"
    ]
    config_output = net_connect.send_config_set(config_commands)
    print("Configuration de l'interface loopback :")
    print(config_output)

    # Fermer la connexion
    net_connect.disconnect()
    print("Connexion fermée.")

except Exception as e:
    print(f"Une erreur s'est produite : {e}")
