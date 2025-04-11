import socket
import threading

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if msg.lower() == 'exit':
                print("[-] Server disconnected.")
                break
            print("\nServer:", msg)
        except:
            break

def send_messages(sock):
    while True:
        msg = input()
        sock.send(msg.encode())
        if msg.lower() == 'exit':
            break

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5000))
print("[+] Connected to server at 127.0.0.1:5000")

# Start two threads: one for receiving, one for sending
threading.Thread(target=receive_messages, args=(client_socket,)).start()
threading.Thread(target=send_messages, args=(client_socket,)).start()
