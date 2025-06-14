import socket
import logging

logging.basicConfig(filename="honeypot.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def honeypot_server():
    host = "0.0.0.0"  # Listen on all interfaces
    port = 8080  # Common decoy port

    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    logging.info(f"Honeypot active on port {port}")

    while True:
        conn, addr = server_socket.accept()
        logging.info(f"Connection from {addr}")
        
        # Simulated fake response
        conn.sendall(b"Welcome to secure server!\n")
        data = conn.recv(1024)

        if data:
            logging.info(f"received data from {addr}: {data.decode()}")
        conn.close()

if __name__ == "__main__":
    honeypot_server()
