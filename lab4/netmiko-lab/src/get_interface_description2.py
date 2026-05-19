from netmiko import ConnectHandler

r1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",
    "username": "student",
    "password": "Meilab123",
    "port": 22
}

r2 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.102",
    "username": "student",
    "password": "Meilab123",
    "port": 22
}

r3 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.103",
    "username": "student",
    "password": "Meilab123",
    "port": 22
}

r4 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.104",
    "username": "student",
    "password": "Meilab123",
    "port": 22
}

for device in (r1, r2, r3, r4):

    net_connect = ConnectHandler(**device)

    print("\n" + "=" * 100)
    print("Connected to:", device["ip"])
    print("=" * 100)

    # Show IP Interface Brief
    output1 = net_connect.send_command("show ip interface brief")
    print("\nSHOW IP INTERFACE BRIEF\n")
    print(output1)

    # Show Version
    output2 = net_connect.send_command("show version")
    print("\nSHOW VERSION\n")
    print(output2)

    # Show Running Configuration
    output3 = net_connect.send_command("show running-config")
    print("\nSHOW RUNNING-CONFIG\n")
    print(output3)

    net_connect.disconnect()
