from email import message
import socket

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)

    while True:
        client, address = server.accept()
        print(f'Connection Established - {address[0]}:{address[1]}')

        received_data = client.recv(1024)
        data = received_data.decode("utf-8")

        ##############################################
        dlist = list(data)

        # getting the number of packets the message contained
        lg = int(dlist[-1])

        del dlist[-1]

        decoded = []
        code = list(dlist[-(lg):])
        # Deleting the appended data to the message that was received
        del dlist[-(lg+2):]

        # Retrieving packets that were received
        packets = []
        for x in range(lg):
            packets.append(dlist[0:5])
            del dlist[0:5]

        # reordering the packets by combining the two lists packets and code
        merged = dict(zip(code, packets))

        sorted_list = {k: v for k, v in sorted(
            merged.items(), key=lambda v: v[0])}

        t = list(sorted_list.values())

        original_data = ""
        for char in t:
            original_data += ''.join(char)

        print(f'Recieved packets: {packets}')

        print(f'Original data: {original_data}')

        ##################################################

        client.close()
