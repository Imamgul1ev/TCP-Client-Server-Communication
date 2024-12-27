import socket

PORT = 5050
FORMAT = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())  # Get local machine's IP address

if __name__ == "__main__":

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))
    string = input("Enter string: ")
    
    client.send(bytes(string, FORMAT))
    
    buffer = client.recv(1024)  # Specify buffer size for receiving data
    buffer = buffer.decode(FORMAT)  # Decode the received bytes into a string
    print(f"Server: {buffer}")

    client.close()
