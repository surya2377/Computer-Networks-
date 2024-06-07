import socket

def sender():
    host = '127.0.0.1'
    port = 12345

    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver_address = (host, port)

    packets = ["Packet0", "Packet1", "Packet2", "Packet3", "Packet4"]

    for packet in packets:
        sender_socket.sendto(packet.encode('utf-8'), receiver_address)
        print(f"Sent: {packet}")

    sender_socket.close()

if __name__ == "__main__":
    sender()
