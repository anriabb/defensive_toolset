from modules import port_scanner, packet_sniffer

def main():
    print(" ")
    print("     =======================")
    print("     === Defensive Suite ===")
    print("     =======================")
    print(" ")

    print("1. Port Scanner")
    print("2. Packet Sniffer")
    print("_______________________")
    response = input("Enter the tool: ")

    #port scanner
    if response == "1":
        print(" ")
        print("#--Port Scanner--#")
        host = input("Enter host: ")
        start_port = int(input("Start port: "))
        end_port = int(input("End port: "))
        ports = range(start_port, end_port + 1)
        open_ports = port_scanner.scan_ports(host, ports)
    elif response == "2":
        try:
            packet_sniffer.run_sniffer()
        except PermissionError:
            print("Permission denied. Run this script as root (sudo) to use the sniffer.")
    


if __name__ == "__main__":
    main()
