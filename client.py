import socket
import random

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Binding the Ip Address and Port Number to one string (address)
    server.connect((ip, port))

    # Capturing User input to be delivered
    file = input("Enter the file name to send: ")
    send_file = open(file, "r")
    data = send_file.read()

    # #closing the file
    send_file.close()

    # converting data to list
    data = list(data)


    # Function to convert data from file into packets
    def split_to_packets(data):
        packets = []

        # Splitting the message into data packets of desired length
        lg = len(data)//5

        # Testing if the number of characters in the string are divisible by 5
        if (len(data) % 5 != 0):
            lg += 1

        i, j = 0, 5
        for x in range(lg):
            packets.append(data[i:j])
            del data[i:j]

        # Genertating Random packets as they are sent over the network
        enc = []
        for x in range(lg):
            enc.append(x)
        random.shuffle(enc)

        # distorting the data packets
        distorted = []
        for x in enc:
            distorted.append(packets[x])

        message = ""
        for x in distorted:
            message += ''.join(x)

        code = map(str, enc)
        message = f"{message}:{''.join(code)}{lg}"

        return message

    # test = f"Original: {output1} \nRecieved Packets:{message}"
    # print(test)
    # print(message[-(lg+2):])
    # print(f"Sent data: {distorted}:{''.join(code)}")
    server.send(bytes(split_to_packets(data), "utf-8"))
