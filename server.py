import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if msg.lower() == 'exit':
                print("[-] Client disconnected.")
                break
            print("\nClient:", msg)
        except:
            break

def send_messages(client_socket):
    while True:
        msg = input()
        client_socket.send(msg.encode())
        if msg.lower() == 'exit':
            break

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5000))
server_socket.listen(1)
print("[*] Listening on 127.0.0.1:5000 ...")

client_socket, addr = server_socket.accept()
print(f"[+] Connection from {addr}")

# Start two threads: one for receiving, one for sending
threading.Thread(target=receive_messages, args=(client_socket,)).start()
threading.Thread(target=send_messages, args=(client_socket,)).start()
