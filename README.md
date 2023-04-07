# Super Simple File Transfer

## Description

A simple and ligthweight client/server app used to transfer files between hosts. The client and server can both be run in reversed mode, to bypass the clients inbound firewall rules, which means that the server sends a file to the client instead. Both the server and client apps terminate after the sending/reveiving of the file so it's a one and done type of app and needs to be rerun for every file if you wish to send more than one.

Absolutely no error handling done. Which means: if it works, it works. If it doesn't, it doesn't...
Should be fully python 2.7 compatible alswell as 3.10.5 (and probably all python3 versions).

## Getting Started

Download all the dependecies, then run the app by running the server with ```python server.py``` and running the client with ```python client.py -a "<IP.ADDRESS.GOES.HERE>"``` the server needs to be run before the client for it to be able to connect to anything. 

There is an arbitrary file size limit of approximately 5 MB, change the "max_file_size" variable in the server script if the file needs to be bigger. 

To run receive a file with the client run the same commands but add the -r flag at runtime ie: ```python server.py -r``` and  ```python client.py -a "<IP.ADDRESS.GOES.HERE>" -r``` 

### Dependencies

* Python (developed with v. 3.10.5 should work in all version from 2.7 and up)

The four following files that are used for sending/receiving data
* client_receive (client writes this output (auto generated and always overwritten))
* client_send (client sends this input)
* server_receive (server writes this output (auto generated and always overwritten))
* server_send (server sends this input)
