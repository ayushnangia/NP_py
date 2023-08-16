import socket 
s=socket.socket()
print("Socket created")
port=8080
s.bind(('127.0.0.1',port))
print(f"Socket binded to {port}")

s.listen(5)
print("Socket is listening")
while True:
    c,addr=s.accept()
    print(f"Got connection from {addr}")
    c.send(b"Thank you for connecting")
    c.close()
    break