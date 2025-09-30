import socket, struct

def mac_addr(mac_bytes):
    """Convert bytes to human-readable MAC address."""
    return ':'.join(f'{b:02x}' for b in mac_bytes)

def main():
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    print("Listening for packets...")

    while True:
        raw_data, addr = s.recvfrom(65535)
        length = len(raw_data)
        dest, src, proto = struct.unpack('!6s6sH', raw_data[:14])
        dest_mac = mac_addr(dest)
        src_mac = mac_addr(src)
        eth_proto = socket.ntohs(proto)

        print(f"Ethernet Frame: {src_mac} -> {dest_mac}, Protocol: {eth_proto}, Length: {length}")
        
run_sniffer = main

if __name__ == "__main__":
    main()
