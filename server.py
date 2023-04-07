# 
# Simple file server that listens on its local ip and port 45678 for a single connection.
# Server accepts a single file upload of size = max_file_size ≈ 5MB.
# Files are stored in the same directory and saved as <latest_incoming_file> without a file extension.
#
import socket
import sys


HOST, PORT = "", 45678

max_file_size = 5 * (10 ** 6) 
output_file = "server_receive"
input_file = "server_send"
server_reverse = "-r" in sys.argv

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
server.settimeout(60)

print("Server started on {}:{}".format(socket.gethostbyname(socket.gethostname()), PORT))

client, address = server.accept()
client.settimeout(60)

print("Client connected: {}".format(address))


def receive_file(client):
    print("Receiving a file!")
    finished_before_limit = False
    data = b""
    data_part = b""

    while len(data) < max_file_size:
        data_part = client.recv(4096)
        if not data_part:
            finished_before_limit = True
            break
        data += data_part

    if finished_before_limit and data:
        with open(output_file, "wb") as file:
            file.write(data)
        print("Ok, file saved to disk")
    elif not data:
        print("No data received. Nothing written")
    else:
        print("File too large. Not written to disk!")


def send_file(client):
    print("Sending a file!")
    with open(input_file, "rb") as file:
        client.sendall(file.read())


if server_reverse:
    send_file(client)
else:
    receive_file(client)


client.close()
server.close()

print("Server now closing!")
