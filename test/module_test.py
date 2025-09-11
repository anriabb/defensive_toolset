from modules import port_scanner

def main():
    ports_to_scan = [80, 443, 22]
    open_ports = port_scanner.scan_ports("google.com", ports_to_scan)
    print("Open ports:", open_ports)

if __name__ == "__main__":
    main()
