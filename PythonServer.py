##########################################################
#   Title   : Socket Programming Assignment 1: Web Server
#   Name    : Meir Zeevi
#   File    : PythonServer.py
#   NYU ID  : N11290134
#   Version : 1.0.0
#   Python 3 interpreter
##########################################################

#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket

#Fill in start
serverSocket.bind((gethostbyname(''), 6789))
serverSocket.listen(5)
#Fill in end

while True:
    #Establish the connection

    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    outputdata =     b"Connection: close\r\n" \
                     b"Date: Mon, 17 Sep 2018 01:40:08 GMT\r\n" \
                     b"Server: Apache/2.4.6 (CentOS)\r\n" \
                     b"Last-Modified: Sun, 16 Sep 2018 05:59:02 GMT\r\n" \
                     b"Accept-Ranges: bytes\r\n" \
                     b"Content-Length: 81\r\n" \
                     b"Content-Type: text/html\r\n" \
                     b"\r\n"

    try:


        message = connectionSocket.recv(500)
        filename = message.split()[1]

        f = open(filename[1:],'rb')


        #Send one HTTP header line into socket

        connectionSocket.send(b"HTTP/1.1 200 OK\r\n" + outputdata)

        #Send the content of the requested file to the client

        for i in f:
            connectionSocket.send(i)
        connectionSocket.close()

    except IOError:

        #Send response message for file not found
        connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n" + outputdata + b"<html>\n<body>\n<h1>404 not found!!</h1>\n</body>\n</html>\n")


        #Close client socket
        connectionSocket.close()
serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data