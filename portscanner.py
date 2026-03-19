import socket

ip = input("Enter the IP address to scan: ")

for port in range(1, 1025):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((ip, port))

    if result == 0:
        print("Open port: " + str(port))
        sock.close()
    else:
        print("Closed port: " + str(port))

    sock.close()