import socket

def scan_ports(host, ports):
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))

            if result == 0:
                print(f"[+] port: {port} - status: OPEN")
            else:
                print(f"[-] port: {port} - status: CLOSED")
            
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

#python3 port_scanner.py | grep "open"