import socket, sys, time

no = sys.argv[1]  
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    sock.sendto(f"PING {no}".encode(), ("127.0.0.1", 5000))
    print(f"[{no}] PING enviado")
    time.sleep(3)