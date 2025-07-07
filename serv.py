import socket
import re
from http import HTTPStatus

end_of_stream = '\r\n\r\n'
HOST = "127.0.0.1"
PORT = 5000
def handle_client(connection):
    client_data = ''
    with connection:
        status=200
        while True:
            data = connection.recv(1024)
            print("Received:", data)
            if not data:
               break
            client_data += data.decode()          
            if end_of_stream in client_data:
                break
        headers = client_data.split('\r')
        method = headers[0].split()[0]
        match_headers = re.search(r'Host:.*', client_data, re.DOTALL)
        headers_line = match_headers.group(0)
        match = re.search(r'status=(\d+)', client_data)
        if match:
            status = int(match.group(1) ) 
        else:
            status = 200

        status_code = HTTPStatus(status)        
        # response = (
        #     #f"HTTP/1.0  {status} {status_code.name} \r\n"
        #     f"Request Method: {method}\r\n"
        #     f"Request Sourse: ('{HOST}', {PORT}) \r\n"
        #     f"Responce Status:  {status_code}  {status_code.name} \r\n"
        #     f"{headers_line}\r\n\r\n"
        #         )

        # print(response)
    
        # connection.send(response.encode())   
        response = (
            f"HTTP/1.1 {status} {status_code.phrase}\r\n"
            f"Content-Type: text/plain\r\n"
            f"Connection: close\r\n"
            f"\r\n"
            f"Request Method: {method}\r\n"
            f"Request Source: ('{HOST}', {PORT})\r\n"
            f"Response Status: {status_code} {status_code.name}\r\n"
            f"{headers_line}\r\n"
        )
        connection.send(response.encode()) 

my_addr= socket.gethostname()
with socket.socket() as serverSocket:
    serverSocket.bind((HOST, PORT))

    serverSocket.listen()

    while(True): 
        (clientConnection, clientAddress) = serverSocket.accept()
        handle_client(clientConnection)
        print(f"Sent data to {clientAddress}")

