# 
# Simple client socket app that connects to the simple server.
# REMOVE THIS # Reads settings from file <connection_details.txt> (add at least your server ip/hostname to it!).
# The client tries to connect to localhost if the -a flag is not used to enter a remote IP. 
#
import socket
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-a", metavar="address", default=None, type=str, help="connect to this address")
parser.add_argument("-p", metavar="port", default=None, type=str, help="connect to this port")
parser.add_argument("-f", metavar="file", default=None, type=str, help="path of file to send")
parser.add_argument("-r", action="store_true", help="reverse, ie. receive file instead")
args = parser.parse_args()

#settings_file = "connection_details.txt"
incoming_file = "client_receive"
reverse_file = args.r

# try:
#     with open(settings_file, "r") as file:
#         params = [file.readline().split("=")[1].strip() for _ in range(3)]
# except:
#     params = ["", "", ""]

HOST = args.a or "localhost"
PORT = args.p or 45678

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(60)
client.connect((HOST, int(PORT)))

print("\nNow connected to server.")
input_file = args.f or input("Enter (absolute) file path: ").replace('"', '') if not reverse_file else ""

if reverse_file:
    print("Receiving a file!")
    with open(incoming_file, "wb") as file:
        data = client.recv(4096)
        while data:
            file.write(data)
            data = client.recv(4096)
else:
    print("Sending a file!")
    with open(input_file, "rb") as file:
        client.sendall(file.read())
    #print("File now sent. Status: UNKOWN")

client.close()

print("Client now closed. Shutting down!")
