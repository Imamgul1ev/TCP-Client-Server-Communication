# TCP Server-Client Application

This is a simple Python-based TCP server-client application. The server listens for incoming client connections, receives a string from the client, modifies it by converting it to uppercase, and sends it back to the client.

## Features

- **Server**: Listens on a specific port, receives a string from the client, converts it to uppercase, and sends it back.
- **Client**: Sends a string to the server and prints the modified response (uppercase).

## Requirements

- Python 3.x
- No external libraries required (uses Python's built-in `socket` library)

## File Structure

- `server.py`: The server script that listens for client connections and processes data.
- `client.py`: The client script that sends data to the server and receives the processed response.
