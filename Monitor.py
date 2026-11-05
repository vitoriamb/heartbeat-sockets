import socket, threading, time
TIMEOUT = 8
last_seen = {}  

def checar():
    alertados = set()
    while True:
        time.sleep(1)
        for no, t in list(last_seen.items()):
            if time.time() - t > TIMEOUT:
                if no not in alertados:
                    alertados.add(no)
                    print(f"[ALERTA] O Nó {no} está OFFLINE!")
            else:
                alertados.discard(no)

threading.Thread(target=checar, daemon=True).start()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 5000))
print("Monitor escutando na porta 5000...")

while True:
    msg, _ = sock.recvfrom(1024)
    _, no = msg.decode().split()  
    last_seen[no] = time.time()