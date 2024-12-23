import socket

# Connect to the server
host = 'localhost'
port = 8080

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))

# Send an HTTP GET request
request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
client_socket.send(request.encode())

# Receive the response from the server
response = client_socket.recv(1024)

# Print the server's response
print(response.decode())

# Close the socket connection
client_socket.close()
