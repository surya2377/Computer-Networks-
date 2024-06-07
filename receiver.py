import socket

def receiver():
    host = '127.0.0.1'
    port = 12345

    receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver_socket.bind((host, port))

    expected_seq_num = 0

    while True:
        data, sender_address = receiver_socket.recvfrom(1024)
        packet = data.decode('utf-8')

        if packet == f"Packet{expected_seq_num}":
            print(f"Received: {packet}")
            expected_seq_num += 1

    receiver_socket.close()

if __name__ == "__main__":
    receiver()
