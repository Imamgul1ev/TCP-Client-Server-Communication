import socket

PORT = 5050
FORMAT = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())  # Get local machine's IP address

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server.bind((SERVER, PORT))

    server.listen(5)
    print(f"Server started, listening on {SERVER}:{PORT}")

    while True:

        client, address = server.accept()
        print(f"Connection Established - {address[0]}:{address[1]}")

        string = client.recv(1024)  # Specify buffer size for receiving data
        string = string.decode(FORMAT)  # Decode the received bytes into a string
        
        string = string.upper()

        client.send(bytes(string, FORMAT))

        client.close()
